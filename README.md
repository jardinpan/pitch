# <div align="center"><img src="artwork/pitch.png" alt="Pitch" width="150px"></div>

A digital signal processing experiment on pitch tracking.

## Usage
```python
>>> import pitch
# To read and perform pitch tracking
>>> audio = pitch.read('sample.mp3')
>>> track_data = pitch.track(audio)
# To visualize
>>> track_data.visualize()
```

## Sample
![](docs/sample01-01.png)
![](docs/sample01-02.png)
![](docs/sample02-01.png)
![](docs/sample02-02.png)
