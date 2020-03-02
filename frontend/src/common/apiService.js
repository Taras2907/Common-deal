import { CSRF_TOKEN } from "./csrfToken";

function apiService(endpoint, method, data) {
  const config = {
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": CSRF_TOKEN
    }
  };
  return fetch(endpoint, config).catch(err => console.log(err));
}

export { apiService };
