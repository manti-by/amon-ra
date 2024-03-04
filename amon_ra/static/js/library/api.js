"use strict"

export class Api {
  constructor () {
    this.token = localStorage.getItem('token')
  }

  isAuthenticated() {
    if (!this.token) {
      this.token = localStorage.getItem('token')
    }
    return !!this.token
  }

  getSettings (on_success) {
    fetch('/api/v1/settings/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
      async: true
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          on_success(data)
        })
        return
      }
      console.error('Error loading settings data')
    })
  }

  getUser (on_success, on_error) {
    if (!this.isAuthenticated()) {
      on_error()
      console.log('Call api.login() first before calling api.getSensors()')
      return
    }
    fetch('/api/v1/users/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Token ' + this.token
      },
      async: true
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          on_success(data)
        })
        return
      }
      console.error('Error loading user data')
    })
  }

  getSensors (on_success, on_error) {
    if (!this.isAuthenticated()) {
      on_error()
      console.log('Call api.login() first before calling api.getSensors()')
      return
    }
    fetch('/api/v1/sensors/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Token ' + this.token
      },
      async: true
    }).then(response => {
      if (response.status === 200) {
        response.json().then(data => {
          on_success(data["results"])
        })
        return
      }
      if (response.status === 401) {
        on_error()
        return
      }
      console.error('Error loading sensors data')
    })
  }

  linkTelegram (data, on_success, on_error) {
    if (!this.isAuthenticated()) {
      on_error()
      console.log('Call api.login() first before calling api.linkTelegram()')
      return
    }
    fetch('/api/v1/subscriptions/link/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Token ' + this.token
      },
      body: JSON.stringify(data),
      async: true
    }).then(response => {
      if (response.status === 201) {
        on_success()
        return
      }
      on_error()
    })
  }

  login (data, on_success, on_error) {
    fetch('/api/v1/users/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
      async: true
    }).then(response => {
      if (response.status === 201) {
        response.json().then(data => {
          localStorage.setItem('token', data.token)
          this.token = data.token
          on_success()
        })
        return
      }
      on_error()
    })
  }
}
