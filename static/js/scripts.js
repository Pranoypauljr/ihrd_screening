import users from './file.json' assert{type:'json'};

function load(){ 
    //alert('helllo');
    for(var i=0;i<5;i++){
    var imgs = document.createElement('img');
    imgs.src="static/images/DSCN0029.jpg";
    imgs.alt="no image";
    imgs.height=350;
    imgs.width=350;
    imgs.style="padding:20px";
    document.body.appendChild(imgs);
    br=document.createElement('br')
    document.body.appendChild(br);
    //document.createElement('br');
    }
}