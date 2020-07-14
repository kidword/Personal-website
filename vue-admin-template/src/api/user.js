import request from '@/utils/request'

// 身份认证
export function Auto(data) {
  return request({
    url: '/vue-admin-template/user/login',
    method: 'post',
    data
  })
}

export function login(data) {
  return request({
    url: 'http://192.168.1.169:7000/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: 'http://192.168.1.169:7000/userinfo',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'post'
  })
}
