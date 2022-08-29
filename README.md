
<h1 align="center">
  <br>
  <img src="https://raw.githubusercontent.com/Cecilia-HNguyen/ImagePasswordGenerator/main/img/PassGenLogo.png" alt="ImagePassGen" width="200"></a>
  <br>
  Image Password Generator
  <br>
</h1>

<h4 align="center"> Generate random password using your webcam 

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#usage">Usage</a> •
  <a href="#contact">Contact</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/Cecilia-HNguyen/ImagePasswordGenerator/main/img/PassGen.gif)

## Key Features
* Take temp picture with webcam and convert to hash.
* Randomize hash to create password with specified length.
* Destroy temp file. 
* Can be use with command-line argument or without.   
  
## Prerequisites

* OpenCV
  ```sh
  pip install opencv-python
  ```

## Usage

```bash
# Main Usage
$ python PassGen.py

# Specify the length 
$ python PassGen.py -l,--length [LENGTH]
```



## Contact

Cecilia.Nguyen@psu.edu
## License

MIT
