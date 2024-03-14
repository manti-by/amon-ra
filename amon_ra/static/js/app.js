import { Api } from './library/api.js'
import { _ } from './library/translate.js'
import {getCookie, deleteCookie, registerHandlebarsHelpers} from './library/utils.js'

import { CenteredWidget } from './widgets/centered.js'
import { LoaderWidget } from './widgets/loader.js'

'use strict'

class App {
  constructor (api) {
    this.api = api

    this.user = null
    this.settings = null
    this.sensors = null

    this.container = document.getElementById('container')

    this.loader = new LoaderWidget()
    this.centered = new CenteredWidget()

    this.checkTelegramAuth()

    this.init()
    this.main()
  }

  checkTelegramAuth () {
    let auth = getCookie("telegram_auth"), uuid = getCookie("telegram_uuid")
    if (auth === "OK") {
      this.api.linkTelegram({"uuid": uuid}, () => {
        deleteCookie("telegram_auth")
        deleteCookie("telegram_uuid")
        window.location.reload()
      })
    }
  }

  init () {
    this.api.getSettings((data) => {
      this.settings = data

      if ("serviceWorker" in navigator) {
        navigator.serviceWorker.register("/static/js/worker.js").then(() => {
          navigator.serviceWorker.ready.then((worker) => {
            worker.sync.register("syncdata")
          })
        }).catch((error) => {
          console.log(error)
        })
      }
    })
  }

  main () {
    if (this.api.isAuthenticated()) {
      if (this.user && this.sensors) {
        this.renderDashboard()
      } else {
        this.update()
      }
    } else {
      this.renderLogin()
    }
    this.loader.hide()
  }

  update () {
    this.api.getUser((data) => {
      this.user = data
      this.api.getSensors((data) => {
        this.sensors = data
        this.renderDashboard()
      }, () => {
        this.renderLogin()
      })
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
    this.render("t-dashboard", { sensors: this.sensors})
    if (!this.user["is_telegram_linked"]) {
      document.getElementById("telegram").classList.remove("hidden")
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
}

document.addEventListener('DOMContentLoaded', (event) => {
  registerHandlebarsHelpers()
  window.app = new App(new Api())
})
