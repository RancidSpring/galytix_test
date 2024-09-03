Project Plan:
- [X] Create a structure for the project: create a unified eay of running the scripts and the app from the command line
- [X] Implement the loaders in an abstract way taking into consideration that the source of data might change
- [X] Implement a one time script for loading the data and cleaning the embedded dataset
- [X] Implement the processing classes: embedder, 
- [X] Implement the processing classes: metrics calculator, 
- [ ] Implement the processing classes: similarity finder (needs to be constructed from the script)
- [ ] Implement the tests for the processing classes using pytest (to be done)
- [ ] Implement the user input processor (to be done)
- [ ] Implement the app for allowing the app to calculate the match on the fly (when the similarity finder is ready, it should just use it in combination with the input processor)

- The whole diagram of the project can be found here:
![Alt text](documentation/galytix_diag.png)

To run the project you need to choose from the following run configurations (the order is important):
- load_embeddings: ex. "-p load_embeddings -bin 'data/binary.bin'"
- calculate_file_similarity: ex. "-p calculate_file_similarity"
- run_app: ex. "-p run_app" (it also has a list of configurable parameters for changing the paths)

The parameters can be found in config/config.toml.

The application can be run in two modes:
- By providing the maunally inputted phrases:
  - The input string should start with "manual:"
- By providing a path to CSV or Parquet:
  - The input string should start with "file:"