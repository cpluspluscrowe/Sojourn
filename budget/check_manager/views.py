from django.shortcuts import render
from .forms import CheckForm
from django.contrib.auth.models import  User
from .models import  Check,Cash
from person_manager.models import Person
# Create your views here.
import datetime
import json
from django.http import HttpResponse
today = datetime.datetime.now().strftime("%m-%d-%Y")
def budget_sheet(request):
    template = 'budget.html'
    form = CheckForm(request.POST or None)
    all_names = []
    users = User.objects.all()
    for x in users:
        all_names.append(str(x.first_name) + " " +  str(x.last_name))
    print(all_names)
    if form.is_valid():
        check = form.save(commit = False)
        check.save()
        context = {'form':form}
        return(render(request,template,context))
    context = {'form':form,'date':today,"all_names":all_names}
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
    DesignatedName = request.GET["DesignatedName"].split("_")[:-1]
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    check_string = request.GET['Check_String']
    #"Check_String":s,"Org_String":s2,"Cash_String":s3,"Design_String":s4
    org_string = request.GET['Org_String'].split(" ")
    cash_string = request.GET['Cash_String'].split(" ")
    desig_string = request.GET['Desig_String'].split(" ")
    cash_name = request.GET['Cash_Name'].split("_")[:-1]
    check_name = request.GET['Check_Name'].split("_")[:-1]
    check_number = request.GET['Check_Number'].split(" ")
    org_name = request.GET["Org_Name"].split("_")[:-1]
    orgCheck_name = request.GET['OrgCheck_Value'].split(" ")

    for x in range(len(check_name)):
        print("Check section")
        first_name = check_name[x].split(" ")[0]
        last_name = check_name[x].split(" ")[1]
        if first_name != "First" and last_name != "Last":
            check_num = check_number[x]
            check_str = check_string[x]
            user = User.objects.get(first_name = first_name, last_name = last_name)
            person = Person.objects.get(corresponding_user = user)
            print("person",person)
            #person.total_givings += float(check_str)
            Check.objects.create(person = person,number = check_num , amount = check_str )
            print("success")

    for x in range(len(cash_name)):
        print("Cash section")
        first_name = check_name[x].split(" ")[0]
        last_name = check_name[x].split(" ")[1]
        if first_name != "First" and last_name != "Last":
            first_name = cash_name[x].split(" ")[0]
            last_name = cash_name[x].split(" ")[1]
            cash_num = cash_string[x]
            user = User.objects.get(first_name = first_name, last_name = last_name)
            person = Person.objects.get(corresponding_user = user)
            #person.total_givings += float(cash_num)
            Cash.objects.create(person = person, amount = cash_num )
            print("success")


    context = {}
    template = "base.html"
    return(render(request,template,context))