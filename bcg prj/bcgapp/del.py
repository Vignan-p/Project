def adminp(request):
    if request.method=='GET':
        
        empdat=empdata.objects.all().values()
        sortedUrl = "http://localhost:8000/employees/?s_flag=asc"
        return render(request,'bcgapp/adminp.html',{'empdat':empdat, 'sortedUrl': sortedUrl})
    

   def adminp(request):
    empdat = empdata.objects.all() 
    page = request.GET.get('page', 1)
  
    paginator = Paginator(emplist, 5)
    try:
        empdat = paginator.page(page)
    except PageNotAnInteger:
        empdat = paginator.page(1)
    except EmptyPage:
        empdat = paginator.page(paginator.num_pages)
  
    return render(request, 'bcgapp/adminp.html', { 'empdat': empdat })

