function sendEmails() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var ws = ss.getSheetByName("Sheet1");
  var range = ws.getRange(2,1,ws.getLastRow()-1,6);

  var url = '';
  url += ss.getUrl();
  url+= '?usp=sharing';

  var emailAddress = 'okan@analyticahouse.com@gmail.com';
  var subject = 'AnalyticaHouse Case Study'
  var des = "Hello,\n\nI'm Ayşenur Akdaş. I finished case study. I have shared the google sheet link with you below. The project was really educational project for me. Thank you for that too :) \n\nThanks.\n\nGoogle sheet link: "+ url;
  
  //Sorting by availability value
  range.sort({column:3,ascending:true})
  GmailApp.sendEmail(emailAddress, subject, des);
}
