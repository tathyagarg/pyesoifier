<script lang="ts">
  import "../app.css";
  let text = "";

  async function translate() {
    const input = (document.getElementById("in") as HTMLTextAreaElement).value;

    const headers = new Headers();
    headers.append("Content-Type", "application/json");

    const raw = JSON.stringify({
      code: input,
    });

    const requestOptions = {
      method: "POST",
      headers: headers,
      body: raw,
      redirect: "follow",
    };

    fetch("https://api-pyesoify.tathya.hackclub.app/translate", requestOptions)
      .then((response) => response.json())
      .then((result) => {
        text = result.code;
      })
      .catch((error) => console.error(error));
  }
</script>

<div id="main">
  <h1 id="header">Pyesoify - Make your code a mess.</h1>
  <h2 id="subheader">
    Make sure to read the <a
      id="readme"
      href="https://github.com/tathyagarg/pyesoify/blob/main/README.md#features"
      >README</a
    > to see compatible features.
  </h2>
  <div id="boxes">
    <div>
      <textarea id="in"></textarea>
    </div>
    <div id="out-box">
      <textarea id="out" readonly>{text}</textarea>
    </div>
  </div>
  <button id="esoify" on:click={translate}>Esoify!</button>
</div>

<style>
  #main {
    background-color: var(--bg);
    height: 100vh;

    padding: 1%;
    display: flex;
    flex-direction: column;
    gap: 1em;
    box-sizing: border-box;
  }

  #header {
    text-align: center;
    font-size: 2em;
    margin-bottom: 0;
    margin-top: 1em;
  }

  #subheader {
    margin-top: 0;
    text-align: center;
    font-size: 1.25em;
    color: var(--subtext);
  }

  #readme {
    color: var(--accent);
  }

  #boxes {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80%;

    gap: 2em;
    padding-bottom: 1em;
  }

  #boxes > div {
    height: 100%;
    width: 50%;
    display: flex;
  }

  #boxes > div > textarea {
    flex: 1;
    height: 100%;

    background-color: white;
    border: none;
    font-family: monospace;
    font-size: 2em;
    resize: none;

    background-color: var(--base);
    border-radius: 1%;
    padding: 1%;
    color: var(--text);
  }

  textarea:focus {
    outline: 1px solid var(--accent);
    box-shadow: 0 0 10px 1px var(--accent);
  }

  #esoify {
    display: block;
    margin: 0 auto;

    border: 0;
    font-size: 2em;
    padding: 0.5em 1em;
    border-radius: 1em;

    background-color: var(--base);
    color: var(--text);
    cursor: pointer;

    transition-duration: 0.1s;
  }

  #esoify:hover {
    box-shadow: 0 0 10px 1px var(--accent);
  }

  h1 {
    margin: 0;
  }
</style>
