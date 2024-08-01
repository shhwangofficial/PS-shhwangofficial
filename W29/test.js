const responsePromise = fetch('https://learn.codeit.kr/api/employees')
  .then((response)=>response.json())
    .then(data => console.log(data));