# ConexusAI

## Project Description

Conexus AI is an undergraduate project developed by students from the University of South-Eastern Norway. The project focuses on implementing an AI chatbot to make the retrieval of relevant data from a large database more intuitive. Additionally, it includes features such as displaying data graphically, downloading it as either a .xls or .pdf file, and receiving it directly into one's email.

### University

The project is developed as part of our graduation requirements at the University of South-Eastern Norway.

### Team!

The Conexus AI project is a collaborative effort by a dedicated team of undergraduate students. Meet the team members:

- [Abdel Sadaqi](link-to-profile): Frontend development, data analysis.
- [Kim Eckmann](link-to-profile): Design, full-stack development.
- [Daniel Rasmussen](link-to-profile): Backend development, AI implementation.
- [Kim Olsen](link-to-profile): Full-stack development, AI implementation.

### Company Collaboration

This project was conducted in collaboration with Egde. The project was initiated to further enhance as previous project developed by Egde, and too research further into the implementation of AI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Installation
---------------------------------------------------
**Frontend:**
---------------------------------------------------
To set up the ConexusAI frontend on your local server, follow these steps:

1. Prerequisites:

- Ensure you have Node.js installed on your system (preferably the latest stable version).
- Install the Vite extension by Anthony Fu for enhanced development experience with hot module replacement support.

2. Clone the Repository:
   If you haven't already, clone the project repository to your local machine using:

- git clone [repository_url]
- Replace [repository_url] with the actual URL of the repository.

3. Install Dependencies:
   Navigate to the project directory in the terminal and install the required npm packages:

```bash
npm install
```
4. Run the Development Server:
   Start the local development server by executing:

```bash
npm run dev
```
- This will spin up a Vite server and the application will be available on a local URL, typically http://localhost:3000.

5. Open the Application:

- Access the frontend by opening the local server URL in your web browser.

---------------------------------------------------
**Backend**
---------------------------------------------------

To set up the ConexusAI backend on your local server, follow these steps:
- Ensure you have Python installed on your system (preferably version 3.12 or newer).
- It is recommended to use a virtual environment for Python projects. This keeps dependencies for the project separate and organized.

### Set Up Virtual Environment:
1. Navigate to the backend directory:
```bash
cd path/to/conexusai/backend
```
- Replace path/to/conexusai/backend with the actual path to your backend directory.
2. Create the virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
on winows:
```bash
.\venv\Scripts\activate
```

**Install Dependencies:**
1. Install the required packages:
```bash
pip install -r requirements.txt
```
**Set Up Environment Variables:**
1. Create a .env file in the root of your backend directory and add your environment-specific variables:
```bash
# .env content
OPENAI_API_KEY=your_OPENAI_API_KEY
SERVER_DB=your_server
USERNAME_DB=your_username
PASSWORD_DB=your_password
DATABASE_DB=your_database
```
2. Load the environment variables in your application as needed, typically at the start of your main script.
   
**Set Up Environment Variables:**
1. Create a .env file in the root of your backend directory and add your environment-specific variables:
```bash
# .env content
OPENAI_API_KEY=your_OPENAI_API_KEY
SERVER_DB=your_server
USERNAME_DB=your_username
PASSWORD_DB=your_password
DATABASE_DB=your_database
```
2. Load the environment variables in your application as needed, typically at the start of your main script.
 
**Testing the Endpoints:**
To test the API endpoints locally, you can use Uvicorn, an ASGI server. Run the following command from the root of your backend directory:
1. ```bash
uvicorn main:app --reload
```
After starting the server, your API will be available at http://127.0.0.1:5000 by default.
You can visit this URL in your web browser to interact with the API.
For a more detailed view of available API routes, you can check the automatically generated documentation by navigating to:
2. 
```bash
http://127.0.0.1:5000/docs
```
or
```bash
http://local_URL/docs
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse interdum faucibus iaculis. Nullam suscipit metus sed sem elementum, nec lacinia quam euismod. Mauris in sem nunc. Integer egestas consequat fringilla. Curabitur auctor, nunc porttitor sodales condimentum, massa sapien rhoncus elit, at pretium ex nisl eu velit. Sed ut metus eu mauris viverra feugiat. Etiam vel hendrerit neque, nec tincidunt mauris. Proin egestas sed sem at accumsan. Morbi sagittis lectus tincidunt nunc placerat, vel lobortis risus pharetra. Mauris sit amet justo ex. Proin nulla massa, lacinia eget pellentesque ac, egestas ut nibh. Proin augue lectus, posuere pharetra sollicitudin nec, facilisis a risus. Maecenas ac neque et felis rutrum sollicitudin et id felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse sodales justo nec risus dapibus convallis.

## Usage

Frontend:
The ConexusAI frontend application is structured into various components, each serving a specific purpose within the user interface:

1. ```NavbarSet.svelte```:

- Houses the navigation functionality through the ```ExpandedButton.svelte``` components.
- To modify button functionality, edit the let buttons array found in the ```+page.svelte``` file located under ```src/routes```.

2. ```ExpandedButton.svelte```:

- This is a generic button component designed to be reusable across the application. Button behaviors can be customized via props.

3. ```ChatbotInterface.svelte```:

- Contains the core logic for user interactions with the AI chatbot. This component manages both input and output of the chat interface.

4. Working with Button Methods:

- For defining actions that button components should execute, locate and edit the ```buttonMethods.js``` file within ```src/lib```.

5. ```Icons```:

- Icons used throughout the application are Svelte components and can be found under ```src/lib/icons```.

6. Server Interaction:

- The ```+server.js``` file under ```src/routes/api/posts``` handles the POST requests to the backend. Any modifications to how the frontend communicates with the backend via POST requests should be made here.



Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse interdum faucibus iaculis. Nullam suscipit metus sed sem elementum, nec lacinia quam euismod. Mauris in sem nunc. Integer egestas consequat fringilla. Curabitur auctor, nunc porttitor sodales condimentum, massa sapien rhoncus elit, at pretium ex nisl eu velit. Sed ut metus eu mauris viverra feugiat. Etiam vel hendrerit neque, nec tincidunt mauris. Proin egestas sed sem at accumsan. Morbi sagittis lectus tincidunt nunc placerat, vel lobortis risus pharetra. Mauris sit amet justo ex. Proin nulla massa, lacinia eget pellentesque ac, egestas ut nibh. Proin augue lectus, posuere pharetra sollicitudin nec, facilisis a risus. Maecenas ac neque et felis rutrum sollicitudin et id felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse sodales justo nec risus dapibus convallis.

## License



Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse interdum faucibus iaculis. Nullam suscipit metus sed sem elementum, nec lacinia quam euismod. Mauris in sem nunc. Integer egestas consequat fringilla. Curabitur auctor, nunc porttitor sodales condimentum, massa sapien rhoncus elit, at pretium ex nisl eu velit. Sed ut metus eu mauris viverra feugiat. Etiam vel hendrerit neque, nec tincidunt mauris. Proin egestas sed sem at accumsan. Morbi sagittis lectus tincidunt nunc placerat, vel lobortis risus pharetra. Mauris sit amet justo ex. Proin nulla massa, lacinia eget pellentesque ac, egestas ut nibh. Proin augue lectus, posuere pharetra sollicitudin nec, facilisis a risus. Maecenas ac neque et felis rutrum sollicitudin et id felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse sodales justo nec risus dapibus convallis.

## Acknowledgments

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse interdum faucibus iaculis. Nullam suscipit metus sed sem elementum, nec lacinia quam euismod. Mauris in sem nunc. Integer egestas consequat fringilla. Curabitur auctor, nunc porttitor sodales condimentum, massa sapien rhoncus elit, at pretium ex nisl eu velit. Sed ut metus eu mauris viverra feugiat. Etiam vel hendrerit neque, nec tincidunt mauris. Proin egestas sed sem at accumsan. Morbi sagittis lectus tincidunt nunc placerat, vel lobortis risus pharetra. Mauris sit amet justo ex. Proin nulla massa, lacinia eget pellentesque ac, egestas ut nibh. Proin augue lectus, posuere pharetra sollicitudin nec, facilisis a risus. Maecenas ac neque et felis rutrum sollicitudin et id felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse sodales justo nec risus dapibus convallis.

## Contact

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse interdum faucibus iaculis. Nullam suscipit metus sed sem elementum, nec lacinia quam euismod. Mauris in sem nunc. Integer egestas consequat fringilla. Curabitur auctor, nunc porttitor sodales condimentum, massa sapien rhoncus elit, at pretium ex nisl eu velit. Sed ut metus eu mauris viverra feugiat. Etiam vel hendrerit neque, nec tincidunt mauris. Proin egestas sed sem at accumsan. Morbi sagittis lectus tincidunt nunc placerat, vel lobortis risus pharetra. Mauris sit amet justo ex. Proin nulla massa, lacinia eget pellentesque ac, egestas ut nibh. Proin augue lectus, posuere pharetra sollicitudin nec, facilisis a risus. Maecenas ac neque et felis rutrum sollicitudin et id felis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse sodales justo nec risus dapibus convallis.
