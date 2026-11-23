(function(){
  var btn=document.querySelector('.theme-btn');
  if(btn){btn.addEventListener('click',function(){
    var cur=document.documentElement.dataset.theme==='dark'?'light':'dark';
    document.documentElement.dataset.theme=cur;try{localStorage.setItem('theme',cur);}catch(e){}
  });}
  var ham=document.querySelector('.hamburger'),sb=document.querySelector('.sidebar');
  if(ham&&sb){ham.addEventListener('click',function(){sb.classList.toggle('open');});}
  document.addEventListener('click',function(e){
    if(sb&&sb.classList.contains('open')&&!sb.contains(e.target)&&e.target!==ham&&!ham.contains(e.target))sb.classList.remove('open');
  });
  document.querySelectorAll('.copy-btn').forEach(function(b){
    b.addEventListener('click',function(){
      var code=b.parentElement.querySelector('pre');
      if(!code)return;
      var t=code.innerText;
      (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){
        b.textContent='已复制';b.classList.add('copied');
        setTimeout(function(){b.textContent='复制';b.classList.remove('copied');},1600);
      },function(){b.textContent='请手动复制';setTimeout(function(){b.textContent='复制';},1600);});
    });
  });
  // search
  var box=document.querySelector('.searchbox input'),panel=document.querySelector('.search-results');
  if(!box||!panel)return;var index=[];
  fetch((document.baseURI.replace(/[^/]*$/,''))+'assets/search-index.json').then(function(r){return r.json();}).then(function(d){index=d;}).catch(function(){});
  function render(q){
    if(!q){panel.style.display='none';panel.innerHTML='';return;}
    var ql=q.toLowerCase(),out=[];
    for(var i=0;i<index.length&&out.length<10;i++){
      var it=index[i],score=0;
      if(it.t.toLowerCase().indexOf(ql)>=0)score+=3;
      if(it.c.toLowerCase().indexOf(ql)>=0)score+=1;
      if(score)out.push({t:it.t,u:it.u,c:it.c,s:score});
    }
    out.sort(function(a,b){return b.s-a.s;});
    panel.innerHTML=out.length?out.map(function(o){
      var pos=o.c.toLowerCase().indexOf(ql);
      var snip=pos>=0?o.c.slice(Math.max(0,pos-40),pos+80):o.c.slice(0,120);
      return '<a href="'+o.u+'"><b>'+o.t+'</b><small>…'+snip+'…</small></a>';
    }).join(''):'<div class="search-empty">没有找到相关内容</div>';
    panel.style.display='block';
  }
  box.addEventListener('input',function(){render(box.value.trim());});
  box.addEventListener('focus',function(){if(box.value.trim())render(box.value.trim());});
  document.addEventListener('click',function(e){
    if(!panel.contains(e.target)&&e.target!==box)panel.style.display='none';
  });
})();
