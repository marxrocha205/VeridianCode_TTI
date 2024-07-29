import tensorflow as tf
from keras import layers
from keras import models
def main():
    
    #importa e carrega 
    datagen = ImageDataGenerator(
        rescale= 1./255,   #intervalo [0,1]
        shear_range=0.2,    #aplica cisalhamento
        zoom_range= 0.2,    # aplica zoom aleatorio
        horizontal_flip=True, 
        validation_split= 0.2 # divide os dados para o treinamento
    )
    
    train_data = datagen.flow_from_directory(
        '.\imgs\class1',
        target_size=(128,128),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )
    
    val_data = datagen.flow_from_directory(
        '.\imgs\class1',
        target_size=(128,128),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )
    
    
    
    #Definir Modelo 
    model = Sequential({
        Conv2D(32,(3,3), activation='relu', input_shape=(128,128,3)),  #Aplica 32 filtros 3x3 img in, funcao de ativacao ReLU
        MaxPooling2D(2,2), #Reduz a dimensao
        Flatten(), #Reduz a img in pra uma dimensao
        Dense(64, activation= 'relu'), #Camada conectada, primeira 64 neuronios em reLU segunda somente 1 com saida binaria
        Dense(1, activation="sigmoid")
        
    }) 
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    model.fit(train_data, validation_data=val_data,epochs=10)  
    

    
    
    






if __name__ == "__main__":
    main()