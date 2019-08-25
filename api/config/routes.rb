Rails.application.routes.draw do

  namespace :items do

    # Department Controller
    match '/department', to: 'department#index', via: %i[get]
    post 'department/create'
    put 'department/update'
    delete 'department/destory'

    # Category Controller
    match '/category', to: 'category#index', via: %i[get]
    post 'category/create'
    put 'category/update'
    delete 'category/destory'

    # Item Controller
    match '/item', to: 'item#index', via: %i[get]
    post 'item/create'
    put 'item/update'
    delete 'item/destory'
    get 'item/getcategorylist' => 'item#getcategorylist'
  end

  namespace :reports do

    # Reports Controller
    match '/', to: 'reports#index', via: %i[get]

    # Customers Controller
    match '/customers/topcustomers', to: 'customers#topcustomers', via: %i[get], as: 'topcustomers'

    # Items Controller
    match '/items/topitems', to: 'items#topitems', via: %i[get], as: 'topitems'

    # Sales Controller
    match '/sales/sales-summary', to: 'sales#salessummary', via: %i[get post], as: 'salessummary'
    match '/sales/total-sales', to: 'sales#totalsales', via: %i[get post], as: 'totalsales'

    # Operations Controller
    match '/operations/shift-log', to: 'operations#shiftlog', via: %i[get post], as: 'shiftlog'
    match '/operations/shift-report', to: 'operations#shiftreport', via: %i[get post], as: 'shiftreport'

    # Pulse Controller
    match '/pulse/customer-feedback', to: 'pulse#customerfeedback', via: %i[get post], as: 'customerfeedback'
    match '/pulse/satisfaction-report', to: 'pulse#satisfactionreport', via: %i[get post], as: 'satisfactionreport'
    match '/pulse/nps-report', to: 'pulse#npsreport', via: %i[get post], as: 'npsreport'
  end

  namespace :settings do

    # User Payment Controller
    get 'user_payment/subscription'
    get 'user_payment/billing'
    post 'user_payment/subscription_update'
    get 'user_payment/choose_payment'
    get 'user_payment/confirmation'
    post 'user_payment/choose_payment'
    post 'user_payment/subscription_charge'
    get 'user_payment/subscription_cancel'
    post 'user_payment/charge'

    # Tax Controller
    match '/tax', to: 'tax#index', via: %i[get]
    post 'tax/create'
    put 'tax/update'
    delete 'tax/destory'

    # Employee Controller
    match '/employee', to: 'employee#index', via: %i[get]
    post 'employee/create'
    put 'employee/update'
    delete 'employee/destory'

    # Register Controller
    match '/register', to: 'register#index', via: %i[get]
    post 'register/create'
    put 'register/update'
    delete 'register/destory'

    # Surcharge Controller
    match '/surcharge', to: 'surcharge#index', via: %i[get]
    post 'surcharge/create'
    put 'surcharge/update'
    delete 'surcharge/destory'

    # Discount Controller
    match '/discount', to: 'discount#index', via: %i[get]
    post 'discount/create'
    put 'discount/update'
    delete 'discount/destory'

    # Table Controller
    match '/table', to: 'table#index', via: %i[get]
    post 'table/create'
    put 'table/update'
    delete 'table/destory'

    # Customer Controller
    match '/customer', to: 'customer#index', via: %i[get]
    post 'customer/create'
    put 'customer/update'
    delete 'customer/destory'

    # Settings Controler
    match '/', to: 'settings#index', via: %i[get]
    match '/switch_device', to: 'settings#switch_device', via: %i[get post]
    match '/payment_types', to: 'settings#payment_types', via: %i[get post]
    match '/card_reader', to: 'settings#card_reader', via: %i[get post]
    match '/receipt', to: 'settings#receipt', via: %i[get post]
    match '/edit-shopdetails', to: 'settings#edit_shopdetails', via: %i[get post]
    get 'merchant_auth', to: 'settings#merchant_auth'
    get 'merchant_deauth', to: 'settings#merchant_deauth'
    get 'merchant_setup', to: 'settings#merchant_setup'

    # Profile Controller
    match '/profile', to: 'profile#index', via: %i[get]
    match '/change_password', to: 'profile#change_password', via: %i[get post]
    match '/edit_profile', to: 'profile#edit_profile', via: %i[get post]
    match '/passcode', to: 'profile#passcode', via: %i[get post]
    match '/user-interface', to: 'profile#userinterface', via: %i[get post], as: 'userinterface'
  end

  # Business Controller
  match '/dashboard', to: 'business#dashboard', via: %i[get]
  match '/feedback-dashboard', to: 'business#feedbackdashboard', via: %i[get], as:  'feedbackdashboard'
  match '/add_business', to: 'business#add_business', via: %i[get post]
  get '/change_business/:bid', to: 'business#change_business', as: 'change_business'

  # Receipts Controller
  match '/receipts', to: 'receipts#index', via: %i[get post]
  match '/receipts/receipt-detail', to: 'receipts#receipt_detail', via: %i[post], as: 'receipt_detail'

  # Invoice Controller
  match '/invoices', to: 'invoices#index', via: %i[get post]
  match '/invoices/invoice-detail', to: 'invoices#invoice_detail', via: %i[post], as: 'invoice_detail'

  # User Controller
  match '/signup', to: 'user#signup', via: %i[get post]
  match '/login', to: 'user#login', via: %i[get post]
  match '/logout', to: 'user#logout', via: %i[get]
  match '/forgot_password', to: 'user#forgot_password', via: %i[get post], as: 'forgot_password'
  match '/reset_password/:encrypteddata', to: 'user#reset_password', via: %i[get post], as: 'reset_password'
  match '/verify/:encrypteddata', to: 'user#verify', via: %i[get], as: 'verify'
  match '/user', to: 'user#index', via: %i[get]
  match '/contact', to: 'user#contact', via: %i[get], as: 'contact'

  match "/404", :to => "errors#not_found", :via => :all
  match "/500", :to => "errors#internal_server_error", :via => :all

  root :to => "user#login"

end
