
async function getAuthorData(){
    const response = await fetch('/api/authors');
    return response.json();
}

function loadTable(authors){
    const table = document.querySelector('#result');
    for(let author of authors){
        table.innerHTML += `<tr>
            <td>${author.id}</td>
            <td>${author.fname}</td>
            <td>${author.lname}</td>
            <td>${author.email}</td>
        </tr>`;
    }
}

async function main(){
    const authors = await getAuthorData();
    loadTable(authors);
}

main();