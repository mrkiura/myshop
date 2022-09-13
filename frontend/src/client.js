import config from './config';
import jwtDecode from 'jwt-decode';
import * as moment from 'moment';

const axios = require('axios');


class FastAPIClient {
  constructor(overrides) {
    this.config = {
      ...config,
      ...overrides,
    };
    this.authToken = config.authToken;

    this.login = this.login.bind(this);
    this.apiClient = this.getApiClient(this.config);
  }

  login(username, password) {
    delete this.apiClient.defaults.headers['Authorization'];

    const form_data = new FormData();
    const grant_type = 'password';
    const item = {grant_type, username, password};
    for (const key in item) {
      form_data.append(key, item[key]);
    }

    return this.apiClient
        .post('/auth/login', form_data)
        .then((resp) => {
          localStorage.setItem('token', JSON.stringify(resp.data));
          return this.fetchUser();
        });
  }

  fetchUser() {
    return this.apiClient.get('/auth/me').then(({data}) => {
      localStorage.setItem('user', JSON.stringify(data));
      return data;
    });
  }

  addToCart(product_id) {
    return this.apiClient.post(`/cart/add?product_id=${product_id}`, null).then(({data}) => {
      return data
    });
  }

  clearCart() {
    return this.apiClient.post("/cart/clear", null).then(({data}) => {
      return data
    });
  }

  getCartSummary() {
    return this.apiClient.get("/cart/summary").then(({data}) => {
      return data
    });
  }

  register(email, password, fullName) {
    const registerData = {
      email,
      password,
      full_name: fullName,
      is_active: true,
    };

    return this.apiClient.post('/auth/signup', registerData).then(
        (resp) => {
          return resp.data;
        });
  }

  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }

  getApiClient(config) {
    const initialConfig = {
      baseURL: `${config.apiBasePath}/api/v1`,
    };
    const client = axios.create(initialConfig);
    client.interceptors.request.use(localStorageTokenInterceptor);
    return client;
  }

  getProduct(productId) {
    return this.apiClient.get(`/products/${productId}`);
  }

  getProducts(keyword) {
    const url = keyword ? `/products/search/?keyword=${keyword}` : "/products/"
    return this.apiClient.get(url).then(({data}) => {
      console.log("data ==> ", data)
      return data;
    }).catch((error) => {
      console.log("error", error)
    });
  }
}


function localStorageTokenInterceptor(config) {
  const headers = {};
  const tokenString = localStorage.getItem('token');

  if (tokenString) {
    const token = JSON.parse(tokenString);
    const decodedAccessToken = jwtDecode(token.access_token);
    const isAccessTokenValid =
			moment.unix(decodedAccessToken.exp).toDate() > new Date();
    if (isAccessTokenValid) {
      headers['Authorization'] = `Bearer ${token.access_token}`;
    } else {
      alert('Your login session has expired');
    }
  }
  config['headers'] = headers;
  return config;
}

export default FastAPIClient;
