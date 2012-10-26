<!DOCTYPE html><html><head><meta charset="utf-8">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<title>Pumpkin Pi</title>
<pre id="console"></pre>
<script src="jquery.min.js"></script>

<script type="text/javascript">

    $(document).ready(function() { 

%for f in filedict.keys():
    $('#{{ f }}').click(function() {
        $.ajax({ url: '/control?action=playtrack&track={{ filedict[f] }}',
            cache: false, type: 'GET', success: true
        });
    })
%end

    $('#lighttoggle1').click(function() {
        $.ajax({ url: '/control?action=blinken1',
            cache: false, type: 'GET', success: true
        });
    })
});
</script>
<style>
body { background-color: white; }
pre { font-family: monospace; color: black; }
h2 { color: orange; font-family: 'arial';}
</style>
</head>
<body>
<br>
<pre>
                          /\                           
                         / /                           
                     ___( (___                         
                  .-'(    `' )`-.                      
                ./    `"""""'    \.                    
               /                   \                   
              /                     \                  
             |       /\      /\      |                 
            |       /O_\    /O_\      |                
            |            /\           |                
            |            ~~           |                
             |      \.        ./     |                 
              \      \\/\/\/\//     /                  
               \      \/\/\/\/     /                   
            jgs `\               /'                    
                  `--_________--'                      
</pre>
<h3>Pumpkin Pi control</h3>

%for f in filedict.keys():
    <button id='{{ f }}'>Play {{ filedict[f] }}</button> <br><br>
%end

<button id='lighttoggle1'>Flash lights</button> <br><br>

</body></html>
