<!DOCTYPE html><html><head><meta charset="utf-8">
<meta http-equiv="Content-Script-Type" content="text/javascript">
<title>SCARY</title>
<pre id="console"></pre>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>

<script type="text/javascript">
    $(document).ready(function() { 
    $('#soundtoggle').click(function() {
        $('#status').empty()
        $.ajax({ url: '/control?action=playtrack&track=h.wav',
            cache: false, type: 'GET',
            success: function(data) {
            $('#status').append(data);}
        });
    })
    $('#lighttoggle1').click(function() {
        $('#status').empty()
        $.ajax({ url: '/control?action=blinken1',
            cache: false, type: 'GET',
            success: function(data) {
            $('#status').append(data);}
        });
    })
});
</script>
<style>
        body { background-color: white; }
        pre { font-family: monospace;
              color: black;
        }
        h2 { color: orange;
             font-family: 'arial';}
</style>
</head>
<body>
<h3>Pumpkin Pi control</h3>
<button id='soundtoggle'>Play sound</button> <br><br>
<button id='lighttoggle1'>Flash lights</button> <br><br>
<div id='status'></div>
These are the files:
%for f in files:
{{ f }}
%end

</body></html>

