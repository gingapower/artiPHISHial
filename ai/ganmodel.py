import tensorflow as tf

# Define the input layers
noise_shape = (100,)  # Shape of random noise vector
image_shape = (64, 64, 3)  # Shape of the input image
num_classes = 10  # Number of classes (if using a conditional GAN)

noise_input = tf.keras.layers.Input(shape=noise_shape, name='noise_input')
image_input = tf.keras.layers.Input(shape=image_shape, name='image_input')

# Define the generator
def build_generator(noise_input, image_input, num_classes=None):
    # Concatenate the noise and image inputs
    combined_input = tf.keras.layers.concatenate([noise_input, image_input])

    # Pass the combined input through a series of dense layers
    x = tf.keras.layers.Dense(1024)(combined_input)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.LeakyReLU(alpha=0.2)(x)
    x = tf.keras.layers.Dropout(0.5)(x)

    # Reshape the output of the dense layers into a 3D tensor
    x = tf.keras.layers.Dense(8 * 8 * 256)(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.LeakyReLU(alpha=0.2)(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Reshape((8, 8, 256))(x)

    # Upsample the 3D tensor using transpose convolutional layers
    x = tf.keras.layers.Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.LeakyReLU(alpha=0.2)(x)

    x = tf.keras.layers.Conv2DTranspose(64, (4, 4), strides=(2, 2), padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.LeakyReLU(alpha=0.2)(x)

    x = tf.keras.layers.Conv2DTranspose(32, (4, 4), strides=(2, 2), padding='same')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.LeakyReLU(alpha=0.2)(x)

    # Generate the output image using a convolutional layer
    if num_classes:
        out = tf.keras.layers.Conv2D(3, (3, 3), activation='tanh', padding='same', name='image_output')(x)
        class_label = tf.keras.layers.Input(shape=(1,), dtype='int32', name='class_label')
        label_embedding = tf.keras.layers.Embedding(num_classes, 50)(class_label)
        label_embedding = tf.keras.layers.Dense(8*8)(label_embedding)
        label_embedding = tf.keras.layers.Reshape((8,8,1))(label_embedding)
        merged = tf.keras.layers.Concatenate()([out, label_embedding])
        return tf.keras.models.Model([noise_input, image_input, class_label], merged)
    else:
        out = tf.keras.layers.Conv2D(3, (3, 3), activation='tanh', padding='same', name='image_output')(x)
        return tf.keras.models.Model([noise_input, image_input], out)

# Create the generator
generator = build_generator(noise_input, image_input, num_classes)
