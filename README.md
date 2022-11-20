# Fabric-Defect-Detection

The intention of the system is to identify the fabric that is defected and the
type of defect along with identify the exact regions of defect. The objective is
to provide manufactures with error free fabric and also help to achieve more
profit by employing less manpower. Fabric defect detection is a significant
phase of quality control in textile industry. There can be defects that gets
unnoticed due to human errors. Quality control is an important feature in
the textile industry. This Project proposes an approach to recognize fabric
defects in textile industry for minimizing production cost and time since the
work of inspectors is very tedious and consumes time and cost. Wastage
reduction through accurate and early stage detection of defects in fabrics
is also an important aspect of quality improvement. The investment in
automated fabric defect detection is more than economical when reduction
in labor cost and associated benefits are considered.
The project aims to provide error free fabrics which can be a tedious job
for humans to identify the various type of defect and exact location on the
image. The system has been implemented using CNN inception algorithm,
OpenCV modules, inbuilt Gaussian Filter and Sobel Operators. An inception
network is a deep neural network with an architectural design that consists
of repeating components referred to as Inception modules. To increase the
performance of a neural network, it’s a logical approach to increase the
number of layers(depth) and units/neuron within the layers(width), which
ineffectively creates a more extensive network. Apart from CNN, there are
other methodologies for finding defects like the kNN, SVM etc. Morphological techniques are used to locate the defect region on the image .
There is a structuring element which is positioned at all possible locations in the
image and it is compared with the corresponding neighbourhood of pixels.
