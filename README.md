# Emotion-Driven Cinematic Scene Engine

Type how you feel in plain language and get back a cinematic scene description:
emotion label, a short scene, camera style, lighting, and a 3-color palette.
Scenes can be saved to a local CSV history and visualized as a chart.

## How it works

The user's text is sent to the Groq API (Llama 3.3 70B model). The model is
asked to return JSON with five fields. The UI parses the response and shows
the result, including the colors as visible swatches.

#Authors

Zeynep Kesim — prompt work, scene quality, and the image-generation integration (the new API, the
schema change, the extra error handling).
Mohoshena - The Flask version: routes, templates, static files, and deployment. Also any
small refactoring in data_handler and stats so they behave the same way in both versions.
Both of us : testing the two versions against each other, GitHub, the final presentation and
the demo.


## Project Structure

project/
│
├── main.py              
├── ai_engine.py         
├── image_engine.py      
├── config.py            
├── data_handler.py      
├── stats.py             
├── ui.py                
│
├── app.py               
├── templates/
│   ├── index.html       
│   └── history.html     
├── static/
│   └── style.css        
│
├── requirements.txt     
└── scenes.csv          



## Setup

1. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate          # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Get a free API key from https://console.groq.com/keys and set it as an
   environment variable:

   ```
   export GROQ_API_KEY="your_key_here"
   ```

3. Run the app:

   ```
   python main.py
   ```
4. Running the Desktop App (Tkinter)
python main.py
5. Running the Web App (Flask)
python app.py
Open your browser and go to http://127.0.0.1:5000

## Usage

1. Type how you are feeling in the input box.
2. Click **Generate Scene** — the app calls the API in the background so the
   window stays responsive.
3. The result appears below: emotion, scene, camera style, lighting, and a
   color palette of three swatches.
4. Click **Save Scene** to append the result to `scenes.csv`. The button only
   appears once a scene has been generated.
5. Click **View History** to see a bar chart of your past emotions. If no
   scenes have been saved yet, the app shows a hint in the status line
   instead of opening an empty chart.

## Error handling

The app distinguishes between several failure modes when contacting the
Groq API and shows a targeted message in the output area:

- **Missing or invalid API key** — `Authentication failed. Please check
  your GROQ_API_KEY.`
- **Rate limit exceeded** — `Rate limit reached. Please wait a moment and
  try again.`
- **No internet / cannot reach the service** — `Could not reach the Groq
  service. Check your internet connection.`
- **Other API errors** — the underlying message is shown.
- **Malformed model response** — `The model returned a response that could
  not be parsed as JSON.`

Any unforeseen exception is caught and displayed as `Unexpected error: ...`
so the application never crashes during use.

Dependencies

groq — Groq API client
flask — Web framework
pandas — Data handling and analysis
matplotlib — Emotion history chart

Security Note
Never commit your API key to GitHub. The key is loaded from an environment
variable (GROQ_API_KEY) and config.py is listed in .gitignore.

## AI Usage Disclosure

In line with the principles of academic transparency, this section documents
the role of AI tools in the development of this project.

AI assistance was used in a supporting capacity for the following purposes:

- **Language polishing.** Reviewing and refining the wording of inline
  comments, the user-facing messages displayed by the UI, and the prose of
  this README to improve clarity, grammar, and tone.
- **Documentation drafting.** Generating an initial outline of the README
  structure (sections, ordering), which was then edited and finalized by
  the author.
- **Minor code-level suggestions.** Occasional suggestions for small
  refinements such as variable naming consistency and formatting choices.

All AI-generated content was reviewed, edited, and approved by the author
before being included.
