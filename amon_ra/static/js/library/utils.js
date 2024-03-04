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
