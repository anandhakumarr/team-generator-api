Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.

  # In the development environment your application's code is reloaded on
  # every request. This slows down response time but is perfect for development
  # since you don't have to restart the web server when you make code changes.
  config.cache_classes = false

  # Do not eager load code on boot.
  config.eager_load = false

  # Show full error reports.
  config.consider_all_requests_local = true

  # Enable/disable caching. By default caching is disabled.
  if Rails.root.join('tmp/caching-dev.txt').exist?
    config.action_controller.perform_caching = true

    config.cache_store = :memory_store
    config.public_file_server.headers = {
      'Cache-Control' => 'public, max-age=172800'
    }
  else
    config.action_controller.perform_caching = false

    config.cache_store = :null_store
  end

  # Don't care if the mailer can't send.


  config.action_mailer.perform_caching = false

  # Print deprecation notices to the Rails logger.
  config.active_support.deprecation = :log

  # Raise an error on page load if there are pending migrations.
  config.active_record.migration_error = :page_load

  # Debug mode disables concatenation and preprocessing of assets.
  # This option may cause significant delays in view rendering with a large
  # number of complex assets.
  config.assets.debug = true

  # Suppress logger output for asset requests.
  config.assets.quiet = true

  # Raises error for missing translations
  # config.action_view.raise_on_missing_translations = true

  # Use an evented file watcher to asynchronously detect changes in source code,
  # routes, locales, etc. This feature depends on the listen gem.
  config.file_watcher = ActiveSupport::EventedFileUpdateChecker

  config.action_mailer.delivery_method = :smtp
  config.action_mailer.perform_deliveries = true
  config.action_mailer.raise_delivery_errors = true

  config.action_mailer.smtp_settings = {
    :address => "email-smtp.us-west-2.amazonaws.com",
    :port => 25,
    :user_name => "AKIAIWMG7EBWWQLSFO5Q", #Your SMTP user
    :password => "ArI88MfLtX4NyvqaWwvS6T1NWFpotsyGN5BjXpQm+MNg", #Your SMTP password
    :authentication => :login,
    :return_response=> true
  }  

  config.action_mailer.default_url_options = { host: 'localhost:3001' }

  config.ENV_MODE = 'TEST MODE'

  #Stripe

  config.STRIPE_SECRET = 'sk_test_5KcugfVL2FiXMJhD9hjzBZio'
  config.STRIPE_PUBLISHABLE = 'pk_test_QLvmnZsuBTBfuhdM7Ix7DUl9'
  config.STRIPE_CLIENTID = 'ca_B93qWCBZuGz76A9RKvKo41A2udkQFLYX'

  Stripe.api_key = config.STRIPE_SECRET

  #Paypal

  config.PAYPAL_CLIENTID = 'AehjqePDqkKbU0FDweqwmPpdUS619bpD_CyYjezxMF_4DhhNrEuXv05TGDCHqFiqy5IzNRucUrVodiKh'
  config.PAYPAL_SECRET = 'EN99hE2PJ6ZlLsXVLaVPVcqOblEeoQLZ-aIEWMON293ei9jUfsr3MTCX0kWL_Uwfx2g30t3yWjR54uvE'

  #RazorPay

  config.RAZOR_KEY = 'rzp_test_dVdM6z67djzWLb'
  config.RAZOR_SECRET = '2pDSp0RMmg5mws0ZRgzqXPO0'

  Razorpay.setup(config.RAZOR_KEY, config.RAZOR_SECRET)

end
