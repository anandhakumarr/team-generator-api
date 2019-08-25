Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.

  # Code is not reloaded between requests.
  config.cache_classes = true

  # Eager load code on boot. This eager loads most of Rails and
  # your application in memory, allowing both threaded web servers
  # and those relying on copy on write to perform better.
  # Rake tasks automatically ignore this option for performance.
  config.eager_load = true

  # Full error reports are disabled and caching is turned on.
  config.consider_all_requests_local       = false
  config.action_controller.perform_caching = true

  config.public_file_server.enabled = true
  config.public_file_server.headers = {
    'Cache-Control' => 'public, s-maxage=31536000, maxage=15552000',
    'Expires' => "#{1.year.from_now.to_formatted_s(:rfc822)}"
  }


  # Disable serving static files from the `/public` folder by default since
  # Apache or NGINX already handles this.

  # Compress JavaScripts and CSS.
  config.assets.gzip = true
  config.assets.js_compressor = :uglifier
  config.assets.css_compressor = :sass

  # Do not fallback to assets pipeline if a precompiled asset is missed.
  config.assets.compile = true

  # `config.assets.precompile` and `config.assets.version` have moved to config/initializers/assets.rb

  # Enable serving of images, stylesheets, and JavaScripts from an asset server.
  # config.action_controller.asset_host = 'http://assets.example.com'

  # Specifies the header that your server uses for sending files.
  # config.action_dispatch.x_sendfile_header = 'X-Sendfile' # for Apache
  # config.action_dispatch.x_sendfile_header = 'X-Accel-Redirect' # for NGINX

  # Mount Action Cable outside main process or domain
  # config.action_cable.mount_path = nil
  # config.action_cable.url = 'wss://example.com/cable'
  # config.action_cable.allowed_request_origins = [ 'http://example.com', /http:\/\/example.*/ ]

  # Force all access to the app over SSL, use Strict-Transport-Security, and use secure cookies.
  # config.force_ssl = true

  # Use the lowest log level to ensure availability of diagnostic information
  # when problems arise.
  config.log_level = :debug

  # Prepend all log lines with the following tags.
  config.log_tags = [ :request_id ]

  # Use a different cache store in production.
  # config.cache_store = :mem_cache_store

  # Use a real queuing backend for Active Job (and separate queues per environment)
  # config.active_job.queue_adapter     = :resque
  # config.active_job.queue_name_prefix = "backoffice_#{Rails.env}"
  config.action_mailer.perform_caching = false

  # Ignore bad email addresses and do not raise email delivery errors.
  # Set this to true and configure the email server for immediate delivery to raise delivery errors.
  # config.action_mailer.raise_delivery_errors = false

  # Enable locale fallbacks for I18n (makes lookups for any locale fall back to
  # the I18n.default_locale when a translation cannot be found).
  config.i18n.fallbacks = true

  options = {
    :enabled => true,
    :remove_spaces_inside_tags => true,
    :remove_multi_spaces => true,
    :remove_comments => true,
    :remove_intertag_spaces => false,
    :remove_quotes => false,
    :compress_css => false,
    :compress_javascript => false,
    :simple_doctype => false,
    :remove_script_attributes => false,
    :remove_style_attributes => false,
    :remove_link_attributes => false,
    :remove_form_attributes => false,
    :remove_input_attributes => false,
    :remove_javascript_protocol => false,
    :remove_http_protocol => false,
    :remove_https_protocol => false,
    :preserve_line_breaks => false,
    :simple_boolean_attributes => false,
    :compress_js_templates => false
  }

  config.middleware.use HtmlCompressor::Rack, options

  # Send deprecation notices to registered listeners.
  config.active_support.deprecation = :notify

  # Use default logging formatter so that PID and timestamp are not suppressed.
  config.log_formatter = ::Logger::Formatter.new

  # Use a different logger for distributed setups.
  # require 'syslog/logger'
  # config.logger = ActiveSupport::TaggedLogging.new(Syslog::Logger.new 'app-name')

  if ENV["RAILS_LOG_TO_STDOUT"].present?
    logger           = ActiveSupport::Logger.new(STDOUT)
    logger.formatter = config.log_formatter
    config.logger = ActiveSupport::TaggedLogging.new(logger)
  end

  # Do not dump schema after migrations.
  config.active_record.dump_schema_after_migration = false


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

  config.action_mailer.default_url_options = { host: 'backoffice.shopowner.in' }

  config.ENV_MODE = 'LIVE MODE'

  #Stripe

  config.STRIPE_SECRET = 'sk_live_gQjv7f58txQ5nZOKefNdxFGH'
  config.STRIPE_PUBLISHABLE = 'pk_live_hxvM1FtV446Dc5qKiA0rfunC'
  config.STRIPE_CLIENTID = 'ca_B93qeKWNRDUHJNNJpkKLfOpaNE5ZSpqT'

  Stripe.api_key = config.STRIPE_SECRET

  #Paypal

  config.PAYPAL_CLIENTID = 'AQqbHaOipDLQ9MpCvSmvP68sCu1EwoxW3NZZ0Fqutte9H1W1cyNmm2l59tWM2oaLgA2OunBN8AqbMigg'
  config.PAYPAL_SECRET = 'EPxphSM3OnffWdzdWOKibzYkv30BzF9_WyQrpdIIx1Nd098H7iYV3RJLlaGGavji-EIG-UROjzhWQrkb'

  #RazorPay

  config.RAZOR_KEY = 'rzp_test_dVdM6z67djzWLb'
  config.RAZOR_SECRET = '2pDSp0RMmg5mws0ZRgzqXPO0'

  Razorpay.setup(config.RAZOR_KEY, config.RAZOR_SECRET)

end
