from django.shortcuts import render
from .forms import CheckForm
# Create your views here.
import datetime
import json
from django.http import HttpResponse
today = datetime.datetime.now().strftime("%m-%d-%Y")
def budget_sheet(request):
    template = 'budget.html'
    form = CheckForm(request.POST or None)
    if form.is_valid():
        check = form.save(commit = False)
        check.save()
        context = {'form':form}
        return(render(request,template,context))
    context = {'form':form,'date':today}
    return(render(request,template,context))

def add_js(request):
    print("function started")
    js_to_add =     js_to_add = """
    <script>
          $('.inputName').on('click focusin', function() {
        this.value = '';
      });
      $('.inputMoney').on('click focusin', function() {
        this.value = '';
      });
      $('.inputMoney').on('focusout', function() {
          if(!this.value) {
              this.value = '0.00';
          }else{
              var sum = parseFloat(0);
              for (i = 0; i < $(".check_amnt").length; i++) {
                  sum += parseFloat($(".check_amnt")[i].value);
              }
              $("#check_total")[0].value = parseFloat(sum).toFixed(2);
          }
      });
      $('.org_money').on('focusout', function() {

              var sum = parseFloat(0);
              for (i = 0; i < $(".org_money").length; i++) {
                  sum += parseFloat($(".org_money")[i].value);
              }
              $("#org_total")[0].value = parseFloat(sum).toFixed(2);
      });
      $('.moneyDesignation').on('focusout', function() {

              var sum = parseFloat(0);
              for (i = 0; i < $(".moneyDesignation").length; i++) {
                  sum += parseFloat($(".moneyDesignation")[i].value);
              }
              $("#Designation_Total")[0].value = parseFloat(sum).toFixed(2);
      });
      $('.cash_amnt_col').on('focusout', function() {

              var sum = parseFloat(0);
              for (i = 0; i < $(".cash_amnt_col").length; i++) {
                  sum += parseFloat($(".cash_amnt_col")[i].value);
              }
              $("#Total_Cash")[0].value = parseFloat(sum).toFixed(2);
      });
      $('.inputName').on('focusout', function() {
          if(!this.value) {
              this.value = "First Name";
          }
      });
      </script>
      """
    context = {'js_to_add':js_to_add}
    template = "base.html"
    return(HttpResponse(json.dumps(context),'base.html'))

def save_data(request):
    print("Save Data Function Called")
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    check_string = request.GET['Check_String']
    #"Check_String":s,"Org_String":s2,"Cash_String":s3,"Design_String":s4
    org_string = request.GET['Org_String'].split(" ")
    cash_string = request.GET['Cash_String'].split(" ")
    desig_string = request.GET['Desig_String'].split(" ")
    cash_name = request.GET['Cash_Name'].split(" ")
    check_name = request.GET['Check_Name'].split(" ")
    check_number = request.GET['Check_Number'].split(" ")
    org_name = request.GET["Org_Name"].split(" ")
    orgCheck_name = request.GET['OrgCheck_Value'].split(" ")

    print(check_string)
    print(org_string)
    print(cash_string)
    print(desig_string)
    print(cash_name)
    print(check_name)
    print(desig_string)
    print(cash_name)
    print(check_name)



    context = {}
    template = "base.html"
    return(render(request,template,context))