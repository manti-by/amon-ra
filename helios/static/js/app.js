import { Api } from './library/api.js'
import { _ } from './library/translate.js'
import { registerHandlebarsHelpers, urlB64ToUint8Array } from './library/utils.js'

import { CenteredWidget } from './widgets/centered.js'
import { LoaderWidget } from './widgets/loader.js'

'use strict'

class App {
  constructor (api) {
    this.api = api

    if (localStorage.getItem('sensors')) {
      this.sensors = localStorage.getItem('sensors')
    }

    this.container = document.getElementById('container')

    this.loader = new LoaderWidget()
    this.centered = new CenteredWidget()

    this.init()
  }

  init () {
    this.api.getSettings((data) => {
      this.settings = data

      if ("serviceWorker" in navigator && "PushManager" in window) {
        navigator.serviceWorker.register("/static/js/worker.js").then((registration) => {
          this.registration = registration
          navigator.serviceWorker.ready.then((worker) => {
            worker.sync.register("syncdata")
          })
          registration.pushManager.getSubscription().then((subscription) => {
            if (subscription) {
              this.subscription = subscription
            }
            this.main()
          })
        }).catch((error) => {
          console.log(error)
        })
      }
    })
  }

  main() {
    if (this.api.token) {
      if (this.sensors) {
        this.renderDashboard()
      } else {
        this.update()
      }
    } else {
      this.renderLogin()
    }
    this.loader.hide()

    this.checkMessages()
  }

  createSubscription() {
    if (!this.registration) {
      console.log("No Service Worker is registered")
      return
    }

    Notification.requestPermission().then((result) => {
      if (result !== "granted") {
        console.log("We weren't granted permission.")
        return
      }

      this.registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlB64ToUint8Array(this.settings["push_public_key"])
      }).then((subscription) => {
        this.saveSubscription(subscription)
      }).catch((error) => {
        console.log(error)
      })
    })
  }

  saveSubscription (subscription) {
    this.subscription = subscription
    this.api.saveSubscription(subscription)
    this.renderDashboard()
  }

  deleteSubscription () {
    this.api.deleteSubscription(this.subscription, () => {
      this.subscription = null
      this.renderDashboard()
    })
  }

  update () {
    this.api.getSensors((data) => {
      this.sensors = data
      this.renderDashboard()
    }, () => {
      this.renderLogin()
    })
  }

  render (template, data) {
    this.container.innerHTML = Handlebars.compile(
      document.getElementById(template).innerHTML
    )(data)
  }

  renderDashboard () {
    this.render("t-dashboard", { profile: this.sensors, isSubscribed: !!this.subscription })

    if (this.subscription) {
      document.getElementById("unsubscribe").onclick = event => {
        event.preventDefault()
        this.subscription.unsubscribe().then(() => {
          this.deleteSubscription()
        }).catch((error) => {
          console.log(error)
        })
      }
    } else {
      document.getElementById("subscribe").onclick = event => {
        event.preventDefault()
        this.createSubscription()
      }
    }
  }

  renderLogin () {
    this.render('t-login')

    this.centered.center(
      document.getElementById('login-form')
    )

    document.getElementById('login').onclick = event => {
      event.preventDefault()

      const data = {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
      }

      this.api.login(data, () => {
        this.update()
      }, () => {
        alert(_("Can't login with provided email and password, please try again with different credentials"))
      })
    }
  }

  checkMessages () {
    if (MESSAGES.length) {
      let result = ''

      for (let i = 0; i < MESSAGES.length; i++) {
        result += MESSAGES[i].message + '\n'
      }

      alert(result)
    }
  }
}

document.addEventListener('DOMContentLoaded', (event) => {
  registerHandlebarsHelpers()
  window.app = new App(new Api())
})
