"user strict"

export class Api {
  constructor () {
    if (localStorage.getItem("token")) {
      this.token = localStorage.getItem("token")
    }
  }

  getSensors(on_success, on_error) {
    if (!this.token) {
      on_error()
      console.log("Call api.login() first before calling api.getSensors()")
      return
    }
    fetch("/api/v1/sensors/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + this.token
      },
      async: true,
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          on_success(data)
        })
        return
      }
      if (response.status === 401) {
        on_error()
        return
      }
      console.error("Error loading sensors data")
    })
  }

  getPhotos(on_success, on_error) {
    if (!this.token) {
      on_error()
      console.log("Call api.login() first before calling api.getPhotos()")
      return
    }
    fetch("/api/v1/sensors/photo/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Token " + this.token
      },
      async: true,
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          on_success(data)
        })
        return
      }
      if (response.status === 401) {
        on_error()
        return
      }
      console.error("Error loading photo data")
    })
  }

  login(data, on_success, on_error) {
    fetch("/api/v1/user/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data),
      async: true,
    }).then(response => {
      if (response.status === 201) {
        response.json().then(data => {
          localStorage.setItem("token", data["token"])
          this.token = data["token"]
          on_success()
        })
        return
      }
      on_error()
    })
  }

  register(data, on_success, on_error) {
    fetch("/api/v1/user/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data),
      async: true,
    }).then(response => {
      if (response.status === 201) {
        on_success()
        return
      }
      on_error()
    })
  }
}
