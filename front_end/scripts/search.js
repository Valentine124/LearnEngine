
const searchInput = document.querySelector("#input");
const searchBtn = document.querySelector("#search_btn");
const resTitle = document.querySelector("#resource-header");
const resBody = document.querySelector("#resource-body");

search_btn.onclick = function() {
    const inputValue = searchInput.value;

    resTitle.textContent = 'Searching Topic';
    resBody.textContent = 'Loading...'
    if (inputValue == null || inputValue == "") {
        resTitle.textContent = "No Topic";
        resBody.textContent = "Enter a topic to get resources.";
    } else {
        fetch('http://www.learnengine.com.ng/api/v1/resources/' + inputValue, {method: 'get', mode: 'cors'})
        .then(response => {
            if (response.ok) {
                return response.json()
            }
            resTitle.textContent = 'Error';
            resBody.textContent = 'Check the topic and try again.';
            throw new Error('Something went wrong')
        })
        .then(resources => {
            resTitle.textContent = 'Resources on ' + inputValue;
            resBody.textContent = '';
            for (const [key, value] of Object.entries(resources)) {
                renderResources(value);
            }
        })
        .catch((error) => {
            resTitle.textContent = 'Error';
            resBody.textContent = 'Check your connection and try agin.';
            console.log(error);
        });
    }
};

function renderResources(resources) {
    const div = document.createElement('div');
    const title = document.createElement('h5');
    const description = document.createElement('h6');
    const img = document.createElement('img');
    const type = document.createElement('p');
    const origin = document.createElement('p');
    const url = resources.url;

    div.classList = 'card';
    img.classList = 'card-img';
    title.classList = 'card-title';
    description.classList = 'card-desc';
    type.classList = 'card-type';
    origin.classList = 'card-origin';

    img.src = resources.img;
    title.innerText = `${resources.title}`;
    description.innerText = `${resources.description}`;
    type.innerText = `${resources.type}`;
    origin.innerText = `${resources.origin}`;

    div.appendChild(img);
    div.appendChild(title);
    div.appendChild(description);
    div.appendChild(type);
    div.appendChild(origin);

    resBody.appendChild(div);

    div.onclick  = function() {
        window.location.href = url;
    };
};