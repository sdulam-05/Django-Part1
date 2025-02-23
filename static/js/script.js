// Dropdown Menu Toggle
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");
if (dropdownButton) {
    dropdownButton.addEventListener("click", () => {
        dropdownMenu.classList.toggle("show");
    });
}

// Upload Image Preview
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
    photoInput.onchange = () => {
        const [file] = photoInput.files;
        if (file) {
            photoPreview.src = URL.createObjectURL(file);
        }
    };

// Scroll to Bottom of Conversation
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;

// Popup Action Buttons
const actionButtons = document.querySelectorAll('.action-button');
if (actionButtons) {
    actionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const buttonId = button.dataset.id;
            let popup = document.querySelector(`.popup-${buttonId}`);
            if (popup) {
                button.innerHTML = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                <title>ellipsis-horizontal</title>
                <path d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908z"></path>
                </svg>`;
                return popup.remove();
            }
            const deleteUrl = button.dataset.deleteUrl;
            const editUrl = button.dataset.editUrl;
            button.innerHTML = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
            <title>remove</title>
            <path d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"></path>
            </svg>`;
            popup = document.createElement('div');
            popup.classList.add('popup');
            popup.classList.add(`popup-${buttonId}`);
            popup.innerHTML = `<a href="${editUrl}">Edit</a>
            <form action="${deleteUrl}" method="delete">
                <button type="submit">Delete</button>
            </form>`;
            button.insertAdjacentElement('afterend', popup);
        });
    });
}
