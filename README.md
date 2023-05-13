
# colorization black & white photos

This is an academic project titled "Colorize Black-White Photos" aims to develop a deep learning model that can colorize grayscale images automatically. The project will focus on using neural networks to train a model that can understand the features and patterns present in black-and-white images and generate plausible colorized versions of the same .



<center><p align="center" width="100%"><img src="https://upload.wikimedia.org/wikipedia/fr/d/d9/Logo_ENIS_Sfax.png" /></p></center>

    



## Presentaion & Code
* [Presentation pptx](https://github.com/youssefboutaleb/colorizeblack-whitephotos/blob/main/presentation.pptx)
* [Presentation online](https://docs.google.com/presentation/d/15d1LXDYWyUhgxngPRQK8sQKjRysBcKfTF4qqER584Z4/edit?usp=sharing)
* [Code.ipynb](https://github.com/youssefboutaleb/colorizeblack-whitephotos/blob/main/Notebook.ipynb)
* [Colab](https://colab.research.google.com/drive/1d7gkoocjpD1QvpGxK9Vm7seTZDSqB0Wj?usp=sharing)
## Alpha Version
This is a great starting point to get a hang of the moving pieces. How an image is transformed into RGB pixel values and later translated into LAB pixel values, [changing the color space](https://ciechanow.ski/color-spaces/). It also builds a core intuition for how the network learns. How the network compares the input with the output and adjusts the network. 

<p align="center"><img src="/README_images/alpha.png?raw=true" width="747px"></p>

In this version, you will see a result in a few minutes. Once you have trained the network, try coloring an image it was not trained on. This will build an intuition for the purpose of the later versions. 

## Beta Version
The network in the beta version is very similar to the alpha version. The difference is that we use more than one image to train the network. I'd recommend running to see how different batch sizes affect your computer's memory. 

<p align="center"><img src="/README_images/beta.PNG?raw=true" width="745px"></p>

For this model, I'd go with a this [cryptopunks dataset](https://huggingface.co/datasets/huggingnft/cryptopunks) .Note that it takes me more than 4 hours to run this.


## Full Version
The full version adds information from a pre-trained classifier. You can think of the information as 20% nature, 30% humans, 30% sky, and 20% brick buildings. It then learns to combine that information with the black and white photo. It gives the network more confidence to color the image. Otherwise, it tends to default to the safest color, brown.

The model comes from an elegant insight by [Baldassarre and his team.](https://github.com/baldassarreFe/deep-koalarization)

<p align="center"><img src="/README_images/full.PNG?raw=true" width="750px"></p>

I
For this model, I'd go with a this [Linnaeus 5 dataset ](http://chaladze.com/l5/)
You'll start getting some results after about 12 - 24 hours on a GPU. 


## GAN Version
The GAN version uses Generative Adversarial Networks to make the coloring more consistent and vibrant. However, the network is a magnitude more complex and requires more computing power to work with. Many of the techniques in this network are inspired by the brilliant work of [Jason Antic](https://github.com/jantic) and his [DeOldify](https://github.com/jantic/DeOldify) coloring network. 

In breif, the generator comes from the [pix2pix model](https://arxiv.org/abs/1611.07004), the discriminators and loss function from the [pix2pixHD model](https://github.com/NVIDIA/pix2pixHD), and a few optimizations from the [Self-Attention GAN](https://arxiv.org/abs/1805.08318). If you want to experiment with this approach, I'd recommend starting with [Erik Linder-Norén](https://github.com/eriklindernoren)'s excellent [pix2pix](https://github.com/eriklindernoren/Keras-GAN/tree/master/pix2pix) implementation. 

<p align="center"><img src="/README_images/gan.png?raw=true" width="747px"></p>

**Implementation details:**
- With a 16GB GPU, you can fit 150 images that are 128x128 and 25 images that are 256x256. 
- The learning improved a magnitude faster on the 128x128 images compared to the 256x256 images.
- I'd recommend experimenting with pre-trained U-nets (One of the secrets in Jason's model)
- Test different normalizations. I prefer spectral normalization, but I've also added instance normalization.
- The network uses 3 discriminators for different image resolutions, based on the pix2pixHD paper. However, this might be overkill, 

- The image generator has some memory problems. Perhaps go with the original generator in Keras or find something equivalent. 
- If you want to build your own dataset, I've inluded a few scraping and cleaning scripts 