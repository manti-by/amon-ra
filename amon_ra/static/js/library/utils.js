import { _ } from './translate.js'

"use strict"


export function registerHandlebarsHelpers () {
  Handlebars.registerHelper({
    translate: (string) => _(string),
    eq: (v1, v2) => v1 === v2,
    ne: (v1, v2) => v1 !== v2,
    lt: (v1, v2) => v1 < v2,
    gt: (v1, v2) => v1 > v2,
    lte: (v1, v2) => v1 <= v2,
    gte: (v1, v2) => v1 >= v2,
    and () {
      return Array.prototype.every.call(arguments, Boolean)
    },
    or () {
      return Array.prototype.slice.call(arguments, 0, -1).some(Boolean)
    },
    telegram_js: (auth_url) => {
      return `<script async src="https://telegram.org/js/telegram-widget.js?22" ` +
        `data-telegram-login="amon_ra_portal_bot" data-size="medium" ` +
        `data-auth-url="` + auth_url + `" data-request-access="write">` +
        `</script>`
    }
  })
}

export function getCookie (name) {
  let nameEQ = name + "="
  let cookies = document.cookie.split(';')
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i]
    while (cookie.charAt(0) === ' ') cookie = cookie.substring(1, cookie.length)
    if (cookie.indexOf(nameEQ) === 0) return cookie.substring(nameEQ.length, cookie.length)
  }
  return null
}

export function setCookie (name, value, days) {
  let expires = ""
  if (days) {
    let date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000))
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + value + expires + "; path=/"
}

export function deleteCookie (name) {
  document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT; path=/'
}
