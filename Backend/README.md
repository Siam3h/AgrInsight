# Agri Insight API Documentation

Welcome to the Agri Insight API documentation. The Agri Insight API provides access to a suite of endpoints designed to support a machine learning platform for agricultural purposes. Through this API, users, including farmers and agricultural enthusiasts, can leverage various features such as crop recommendations, crop yield prediction, and access to best farming practices. Below is an overview of the available endpoints and their functionalities.

## Endpoints

### Crop Recommendations

- **Endpoint:** `/api/v1/crop-recommendations/`
- **Method:** POST
- **Description:** This endpoint allows users to receive crop recommendations based on various factors such as soil type, climate conditions, and historical crop performance data. Users can provide input parameters, and the API will return recommended crops along with relevant information.

### Crop Yield Prediction

- **Endpoint:** `/api/v1/crop-yield-prediction/`
- **Method:** POST
- **Description:** This endpoint enables users to predict crop yields for specific crops and regions. Users can input parameters such as crop type, soil quality, weather conditions, and agricultural practices to receive yield predictions. The API utilizes machine learning algorithms to provide accurate yield estimates.

### Best Farming Practices

- **Endpoint:** `/api/v1/best-farming-practices/`
- **Method:** GET
- **Description:** This endpoint provides access to a curated collection of best farming practices and agricultural techniques. Users can retrieve information on optimal planting times, irrigation methods, fertilization techniques, pest control strategies, and more. The API delivers valuable insights to help farmers improve their farming practices and maximize yields.

## Authentication & Profile Management

- **Authentication:** Django Built Token-based authentication 
- **Permissions:** Certain endpoints may require specific permissions for access. Users need to authenticate and possess the necessary permissions to interact with protected endpoints.

- **Endpoint:** `api/v1/accounts/auth/signup/`
- - **Method:** POST

- **Endpoint:** `api/v1/accounts/auth/login/`
- - **Method:** POST

- **Endpoint:** `api/v1/accounts/auth/logout/`
- - **Method:** POST

- **Endpoint:** `api/v1/accounts/update_profile/`
- - **Method:** PUT
    
- **Endpoint:** `api/v1/accounts/delete_account/`
- - **Method:** DELETE
    
- **Endpoint:** `api/v1/accounts/auth/test_token/`
- - **Method:** GET

## Response Formats

- **Data Format:** JSON
- **Error Handling:** The API returns appropriate error responses with detailed error messages in case of invalid requests or server-side errors.

---
## License

This project is licensed under the [Agri Insight API License](LICENSE.md). Please review the license terms before using the API.
