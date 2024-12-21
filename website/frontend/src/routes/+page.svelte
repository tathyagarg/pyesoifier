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

    fetch("http://0.0.0.0:6060/translate", requestOptions)
      .then((response) => response.json())
      .then((result) => {
        text = result.code;
      })
      .catch((error) => console.error(error));
  }
</script>

<div id="main">
  <h1 id="header">Pyesoify - Make your code a mess.</h1>
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
    background-color: red;
    height: 100vh;

    padding: 1%;
    display: flex;
    flex-direction: column;
    gap: 1em;
    box-sizing: border-box;
  }

  #header {
    text-align: center;
    line-height: 10vh;
  }

  #boxes {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90%;

    gap: 2em;
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
  }

  #esoify {
    display: block;
    margin: 0 auto;

    border: 0;
    font-size: 2em;
    padding: 0.5em 1em;
    border-radius: 1em;
  }

  h1 {
    margin: 0;
  }
</style>
