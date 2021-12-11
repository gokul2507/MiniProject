function displaydetails(x,url) {
     var f = document.createElement('form');
     f.action=url;
     f.method='POST';

     var i=document.createElement('input');
     i.type='hidden';
     i.name='id';
     i.value=x.id;
     f.appendChild(i);
     
     document.body.appendChild(f);
     f.submit();
}