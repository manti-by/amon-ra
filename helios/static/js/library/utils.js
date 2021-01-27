import { _ } from "./translate.js"

"use strict"

export function installServiceWorker() {
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register('./worker.js', {scope: './'}).then((reg) => {
      console.debug("Registration succeeded. Scope is " + reg.scope);
    }).catch((error) => {
      console.error("Registration failed with " + error);
    });
  }
}

export function registerHandlebarsHelpers() {
  Handlebars.registerHelper({
    "translate": (string) => _(string),
    "eq": (v1, v2) => v1 === v2,
    "ne": (v1, v2) => v1 !== v2,
    "lt": (v1, v2) => v1 < v2,
    "gt": (v1, v2) => v1 > v2,
    "lte": (v1, v2) => v1 <= v2,
    "gte": (v1, v2) => v1 >= v2,
    and() {
        return Array.prototype.every.call(arguments, Boolean)
    },
    or() {
        return Array.prototype.slice.call(arguments, 0, -1).some(Boolean)
    }
  })
}
