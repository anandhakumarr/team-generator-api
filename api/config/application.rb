require_relative 'boot'

require 'rails/all'

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

ENV['EMAIL_SENDER_ADDRESS'] = "\"ShopOwner POS\" <noreply@backoffice.shopowner.in>"
ENV['EMAIL_TO_ADDRESS'] = 'support@shopowner.in '
ENV['APP_NAME'] = 'shopowner-backoffice'
ENV['APP_VERSION'] = 'v1.3'

if Rails.env.production?
		Raven.configure do |config|
	 		config.dsn = 'https://f5836d319c634a2b8cbccb633070bd31:60367f64277e49018b90e65a1a00dba5@sentry.io/256450'
		end
elsif Rails.env.alpha? or Rails.env.beta?
	Raven.configure do |config|
			config.dsn = 'https://76ab2319611646ec941704cb4c4c27d7:8848568e790c4706984ec53d324aa695@sentry.io/1209842'
	end
end


module Backoffice
  class Application < Rails::Application
    # Settings in config/environments/* take precedence over those specified here.
    # Application configuration should go into files in config/initializers
    # -- all .rb files in that directory are automatically loaded.
  end
end
