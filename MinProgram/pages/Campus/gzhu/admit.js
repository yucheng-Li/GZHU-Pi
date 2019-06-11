const Page = require('../../../utils/sdk/ald-stat.js').Page
Page({


  data: {

  },


  onLoad: function(options) {
    this.admitQuery()
  },


  onShareAppMessage: function() {

  },


  admitQuery() {
    let url = "http://localhost:5000/admit_query"
    wx.request({
      url: url + "?stu_id=***REMOVED***" + "&stu_name=***REMOVED***",
      method: "get",
      header: {
        'content-type': 'application/x-www-form-urlencoded'
      },
      success: function(res) {
        console.log(res)
      }
    })
  }

})