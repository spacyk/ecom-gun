# Eshop Recipe

This is a generic purpose e-commerce web application created with Django web framework
with aim to provide out of the box eshop template with some useful integrations.

This project is based on online course.
https://www.udemy.com/course/build-an-e-commerce-website-with-django/learn/lecture/16261354#overview

**However, there are interesting extensions that are out of the scope of the course.**

### Current Extentions
 - Integration with **aws S3** data storage to store product images.
 - Partially done integration with **Stripe** card payment method to handle payments for the products.

**Beware there are many things that need to be refactored, fixed, updated or finished before deployment to production.**

### Future Ideas
**Customer**
 - Make signup and login only possible with email.
 - Add user profile interface.

**Orders**
 - Extend and update order properties.
 - Improve Order management - Keep track of refunds. Properly review and set up the order flow.

**Payments**
 - Create payment model - save payment intent data.
 - Handle all payment responses - success, timeout, wrong data, errors. Use stripe test cases.
 - Store card information for future payments.

**Other**
 - Extend address fields to allow different billing and shipping address.
 - Create custom admin actions for "bulk" order updates.

