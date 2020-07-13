// const qxdata = [
//   { 'name': '朝阳市气象局', 'content': '雷雨大风蓝色预警信号：预计未来4到6小时，朝阳地区将出现雷雨大风天气，阵风风力可达7到8级，同时可能伴有冰雹、短时强降水等强对流天气，请注意防范。朝阳市气象台2020年7月13日12时45分发布', 'type': '雷雨大风', 'location': '辽宁', 'level': '蓝色', 'display_time': '2020-07-13 12:48:42' }
// ]

const qxdata = [
  { 'name': '新街口花园', 'model': '3室2厅', 'area': '91', 'toward': '南', 'decorate': '简装', 'positionInfo': '高楼层(共12层) 2004年建塔楼', 'time': '2020-05-19', 'price': '86725', 'res_price': 488 }
]

module.exports = [
  {
    url: '/vue-admin-template/table/list',
    type: 'get',
    response: config => {
      const items = qxdata
      return {
        code: 20000,
        data: {
          // total: items.length,
          items: items
        }
      }
    }
  }
]
