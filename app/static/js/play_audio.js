console.log(">>>>>>>>>>>>>>>>>>>>")
function playAudio() {
    let audioUrl = document.getElementById('audio-url').value;
    console.log('Audio URL:', audioUrl); // Debug statement
    let newWindow = window.open("", "_blank");
    newWindow.document.write(`
        <audio id="audio" autoplay>
            <source src="${audioUrl}" type="audio/mpeg">
        </audio>
        <script>
            var audio = document.getElementById('audio');
            audio.onended = function() {
                window.close();
            };
        <\/script>
    `);
}
