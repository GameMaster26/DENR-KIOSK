window.addEventListener('load', () => {
  const aiContainer = document.getElementById('aiIcon');
  const aiButton = document.getElementById('aiButton');

  const message = "Hello! Welcome to PENRO Kiosk. How can I assist you today?";
  const synth = window.speechSynthesis;
  const utter = new SpeechSynthesisUtterance(message);
  utter.lang = 'en-US';
  utter.pitch = 1.2;
  utter.rate = 0.95;
  utter.volume = 1;

  function setFemaleVoiceAndSpeak() {
    const voices = synth.getVoices();
    const femaleVoice = voices.find(voice =>
      voice.name.toLowerCase().includes("female") ||
      voice.name.includes("Google US English") ||
      voice.name.includes("Jelisa") ||
      voice.name.includes("Microsoft Zira")
    );
    if (femaleVoice) {
      utter.voice = femaleVoice;
    }
    synth.speak(utter);
  }

  if (aiContainer && aiButton) {
    aiContainer.classList.add('show');

    // Trigger voice after voices load
    synth.onvoiceschanged = () => {
      setFemaleVoiceAndSpeak();
    };

    // Also allow replay on click
    aiButton.addEventListener('click', () => {
      if (!synth.speaking) {
        setFemaleVoiceAndSpeak();
      }
    });
  }
});
