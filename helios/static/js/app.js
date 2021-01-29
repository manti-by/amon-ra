import { Api } from "./library/api.js"
import { _ } from "./library/translate.js"
import { registerHandlebarsHelpers, installServiceWorker } from "./library/utils.js"

import { CenteredWidget } from "./widgets/centered.js"
import { LoaderWidget } from "./widgets/loader.js"


"user strict"

class App {
  constructor (api) {
    this.api = api

    if (localStorage.getItem("sensors")) {
      this.sensors = localStorage.getItem("sensors")
    }

    this.container = document.getElementById("container")

    this.loader = new LoaderWidget()
    this.centered = new CenteredWidget()

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

  update() {
    this.api.getSensors((data) => {
      this.sensors = data
      this.renderDashboard()
    }, () => {
      this.renderLogin()
    })
  }

  render(template, data) {
    this.container.innerHTML = Handlebars.compile(
      document.getElementById(template).innerHTML,
    )(data)
  }

  renderDashboard() {
    this.render("t-dashboard", { profile: this.sensors })
  }

  renderLogin() {
    this.render("t-login")

    document.getElementById("show-registration-form").onclick = event => {
      this.renderRegistration()
    }

    this.centered.center(
      document.getElementById("login-form")
    )

    document.getElementById("login").onclick = event => {
      event.preventDefault()

      let data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
      }

      this.api.login(data, () => {
        this.update()
      }, () => {
        alert(_("Can't login with provided email and password, please try again with different credentials"))
      })
    }
  }

  renderRegistration() {
    this.render("t-register")

    document.getElementById("show-login-form").onclick = event => {
      this.renderLogin()
    }

    document.getElementById("register").onclick = event => {
      event.preventDefault()

      let data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
      }

      this.api.register(data, () => {
        alert(_("Account created successfully, please check you email for verification link."))
        this.renderLogin()
      }, () => {
        alert(_("Can't register with provided email and password, please try again with different credentials"))
      })
    }

    this.centered.center(
      document.getElementById("register-form")
    )
  }

  checkMessages() {
    if (MESSAGES.length) {
      let result = ""

      for (let i = 0; i < MESSAGES.length; i++) {
        result += MESSAGES[i]["message"] + "\n"
      }

      alert(result)
    }
  }
}

document.addEventListener("DOMContentLoaded", (event) => {
  installServiceWorker()
  registerHandlebarsHelpers()

  let api = new Api(),
    app = new App(api)
})
