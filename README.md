# Onlyfakes API

An API wrapper for the onlyfakes website made in python.

Is able to create prompts, submit them and fetch their results.

License: MIT - See the `LICENSE` file.

# Installation

- Install with pip: `pip install onlyfakes`
- Install locally from github: `pip install git+https://github.com/Egsagon/onlyfakes-api.git`

# Usage

Example classic usage:
```python
import onlyfakes as of

# Initialise the session
client = of.Client()

# Create a new prompt
prompt = of.Prompt(
    positive = '<insert positive prompt>',
    negative = '<insert negative prompt>',
    engine = of.Engine.hentai_HD

    # Advanced settings
    width = 512,
    height = 640,
    cfg = 7.5,
    seed = of.Seed( 12345678 )
)

# Submit the prompt and wait for it to process
img = client.generate(prompt)

# Download the image at a specific path
img.download('result.png')
```

Other example using shorthands:
```python
import onlyfakes as of

of.Client().new(prompt = '<fill>', negative_prompt = '<fill>', engine = of.Engine.hentai_HD).generate().download('result.png')
```

The `generate` method contains a loop that breaks when it get a result. You can change its interaction intervals and
maximum by specifying them as arguments. You can also enable verbose to see the current process evolution.
```python
prompt.generate(
    interval = 2 * 60,
    timeout = 4 * 60,
    verbose = True
)
```

If want async or stuff that runs in parallel, you can use the `submit` function that will only send your prompt to the backend.
You will then be able to fetch the image using the `check` method. You can also build your async function.

```python
response = client.submit(prompt)

# Do stuff for 2 min ... 

data = client.check()

if data == False: ... # The backend has not finished yet

# Create the image object from data url
image = of.Image( data['imageUrl'] )
```

## TODO

- Async stuff
- Account handling
- Presets
