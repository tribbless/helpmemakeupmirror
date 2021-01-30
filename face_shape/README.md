<div class="column">
    <img alt="GitHub" src="https://img.shields.io/badge/Tensorflow-2.0-blue.svg">
    <img alt="GitHub" src="https://img.shields.io/badge/Keras-2.2.5-blue.svg">
    <img alt="GitHub" src="https://img.shields.io/badge/Licence-LGPL_v3.0-blue.svg">

# Face Shape Analyzer

Around age 17, I attempted to come up with a way to accurately detect the shape of a person's face. Right now beauty experts use loose guidelines such as the width of the forehead, or the sharpness of the chin to roughly classify a face shape. Here is my process of determining the shape of a person's face.

<!-- wp:heading {"level":3} -->
<h3>Principle</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The human face can be broadly classified into 4 major types. Ofcourse there are plenty of variations because each person is unique. The major face shape categories are:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>Square<br></li><li>Heart <br></li><li>Oval<br></li><li>Round </li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>Method</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Create a Convolution Neural Networks(CNNs) which is trained using celebrity images for each face shape. These will act as benchmarks. </p>
<!-- /wp:paragraph -->

Feed the user's image into the newly trained model. The shape with the highest probability is the user's face shape.

<!-- wp:heading {"level":3} -->
<h3>Implementing Deep Learning</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Neural Network Used: CNN</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Neurons in output layer: 4</p>
<!-- /wp:paragraph -->

# Test
By looking at this photo, you would say that the face shape is oval. This inference can change from person to person. Let's see what result the CNN gives us.

<p align="center">
  <img width="200" height="300" src="https://media.giphy.com/media/Xd270oOTrwL2sHyyrW/giphy.gif">
</p>

# Result

<p align="center">
  <img width="700" height="400" src="https://media.giphy.com/media/TIAHDR5np0G4iTvErr/giphy.gif">
</p>

#### Generated output: Oval

The CNN has analyzed the image and confirmed that it is an oval shaped face.

### Benchmarks:

<!-- wp:heading {"level":4} -->
<h4>Square Face:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Billie Piper</li><li>Demi Moore</li><li>Jennifer Aniston</li><li>Katie Holmes</li><li>Kelly Osborne</li><li>Renee Zellweger</li><li>Sandra Bullock</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Heart Face:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Cheryl Cole</li><li>Eva Longoria-Parker</li><li>Gwyneth Paltrow</li><li>Mary-Kate Olsen</li><li>Naomi Campbell</li><li>Nicole Richie</li><li>Reese Witherspoon</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Oval Face:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Cameron Diaz</li><li>Charlize Theron</li><li>Cindy Crawford</li><li>Courtney Cox</li><li>Elle Macpherson</li><li>Julia Roberts</li><li>Rihanna</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":4} -->
<h4>Round Face:</h4>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Drew Barrymore</li><li>Ginnifer Goodwin</li><li>Hayden Panettiere</li><li>Isla Fisher</li><li>Kate Bosworth</li><li>Mila Kunis</li></ul>
<!-- /wp:list -->

# Dataset

To learn more about the dataset, visit the link below:

https://github.com/prateekmehta59/Celebrity-Face-Recognition-Dataset


# References:
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>Square face shape:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1646/celebrity-face-shapes-square-99685/" rel="nofollow">https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1646/celebrity-face-shapes-square-99685/</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Heart face shape:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1642/celebrity-face-shapes-heart-99644/" rel="nofollow">https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1642/celebrity-face-shapes-heart-99644/</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Oval face shape:</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1644/celebrity-face-shapes-oval-99666/" rel="nofollow">https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1644/celebrity-face-shapes-oval-99666/</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Round face shape: </strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1645/celebrity-face-shapes-round-99677/" rel="nofollow">https://www.cosmopolitan.com/uk/beauty-hair/celebrity-hair-makeup/g1645/celebrity-face-shapes-round-99677/</a></p>
<!-- /wp:paragraph -->


