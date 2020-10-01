Django Rest framework with multilevel Nested framework
OutPut:

    {
  "first_name": "John",
  "last_name": "Robert",
  "instrument": "keyboard",
  "album_musician": [
      {
          "artist": 1,
          "name": "first album",
          "release_date": "2020-09-26",
          "num_stars": 10,
          "place_album": [
              {
                
                  "alname": 1,
                  "placename": "first place",
                  "time": "09:30",
                  "use_place": [
                      {
                          
                          "pluse": 1,
                          "Cameramodel": "Sony",
                          "byyear": "2020-09-26",
                          "Demo_Use": [
                              {
                                 
                                  "Duse": 1,
                                  "Dname": "Demo 1",
                                  "Age": 20
                              }
                          ]
                      }
                  ]
              }
          ]
      }
  ]
}

