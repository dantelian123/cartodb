defaults: &defaults
  # If uncommented, most images like static map previews and twitter card image urls will use this CDN urls
  #cdn_url:
  #  http:             "http.cdn.host"
  #  https:            "https.cdn.host"
  http_client_logs: true
  ogr2ogr:
    binary:           'which ogr2ogr'
    csv_guessing:     true
    memory_limit:
  debug_assets: true
  mandatory_keys:     [layer_opts, sql_api, varnish_management, redis, session_domain]
  session_domain:     '.localhost.lan'
  # If activated, urls will use usernames in format //SESSION_DOMAIN/user/USERNAME and ignore subdomains if present
  subdomainless_urls: false
  http_port:           3000 # nil|integer. HTTP port to use when building urls. Leave empty to use default (80)
  https_port:          # nil|integer. HTTPS port to use when building urls. Leave empty to use default (443)
  secret_token:       '71c2b25921b84a1cb21c71503ab8fb23'
  # It's recommended to generate a new secret_key_base for each installation using `bundle exec rake secret`
  secret_key_base:    '65903fa751affcdd71a9eb09308bcb404c50c8df03414db849ea22fbe8d4aae9ff344f6594630eb9c8367b4fd8ed2211d0342a49df473dccc27ae0be120b25ab'
  # It's recommended to generate a new password_secret (pepper for password encryption) for each installation using `bundle exec rake secret`
  password_secret:    'cc914bbbfa1d7156ec1424260d3a3214f3d1720aae872c1a5887f918929d0fec6f048d708f1ca79b4e43d20b4b623726e656917c9b8f2de0ea6c18e2ee80ce89'
  account_host:       'localhost.lan:3000'
  # Here you can define other hosts different to account_host that also will be CORS enabled
  # cors_enabled_hosts:
  #   - example.com
  #   - foo.bar
  #   - carto.dev
  account_path:       '/account'
  vizjson_cache_domains: ['.localhost.lan']
  data_library:
    username:         'common-data'
    path:             '/data-library'
  disable_file:       '~/disable'
  watcher:
    ttl:              60
  tiler:
    filter: 'mapnik'
    internal:
      protocol:      'http'
      domain:        'localhost.lan'
      port:          '8181'
      host:          '127.0.0.1'
      verifycert:     false
    private:
      protocol:      'http'
      domain:        'localhost.lan'
      port:          '8181'
      verifycert:     false
    public:
      protocol:      'http'
      domain:        'localhost.lan'
      port:          '8181'
      verifycert:     false
  sql_api:
    private:
      protocol:   'http'
      domain:     'localhost.lan'
      endpoint:   '/api/v1/sql'
      port:       8080
    public:
      protocol:   'http'
      domain:     'localhost.lan'
      endpoint:   '/api/v2/sql'
      port:       8080
  api_requests_service_url: ''
  developers_host:    'http://developers.localhost.lan:3000'
  google_analytics:
    primary:          ''
    embeds:           ''
    domain:           ''
  google_tag_manager:
    primary:          ''
    embeds:           ''
  rollbar_api_key: ''
  tumblr:
    api_key: ''
  trackjs:
    enabled: false
    customer: ''
    app_keys:
      editor: ''
      embeds: ''
    frequency: 0.2
  #fullstory:
    #org: 'XXXXX'
  facebook:
    app_id: ''
    admins: ''
  hubspot: ''
  segment:
    api_key:
  pubsub:
      project_id: ''
      credentials: ''
      topic: ''
  passwords:
    expiration_in_d:
    rate_limit:
      max_burst:
      count:
      period:
  metrics:
    hubspot:
      events_host: 'http://track.hubspot.com'
      token: 'yourtoken'
      form_ids:
        newsletter: ''
      event_ids:
        import_failed: ''
        geocoding_failed: ''
        import_success: ''
        geocoding_success: ''
        published_visualization: ''
        visited_dashboard: ''
        connect_dataset: ''
        create_map: ''
        export_table: ''
        export_map: ''
        export_public_map: ''
        select_wms: ''
        color_basemap: ''
        pattern_basemap: ''
        geocoding: ''
        visual_merge: ''
        common_data: ''
        cartocss_manually: ''
        wizard: ''
        filter: ''
        query: ''
        applied_sql: ''
        applied_cartocss: ''
        modified_style_form: ''
        completed_connection: ''
        failed_connection: ''
        created_analysis: ''
        modified_analysis: ''
        published_map: ''
        exported_map: ''
      mailing_track:
        like_map: ''
        trending_map: ''
  common_data:
    protocol: 'https'
    username: 'common-data'
    # base_url: 'https://common-data.carto.com'
    format: 'gpkg'
    generate_every: 86400
  explore_api:
    username: ''
  aggregation_tables:
    host: 'localhost'
    port: '5432'
    dbname: 'dataservices_db'
    username: 'geocoder_api'
    password: ''
    tables:
      admin0: 'ne_admin0_v3'
      admin1: 'global_province_polygons'
  reports:
    mail_to: ''
  mailer:
    from: 'carto.com <support@carto.com>'
    address: ''
    port: ''
    user_name: ''
    password: ''
    authentication: ''
    enable_starttls_auto: ''
    template:
      app_name: 'CARTO'
      app_link: 'https://carto.com'
      header_logo_url: 'http://carto-email-assets.s3.amazonaws.com/carto-logo.png'
      footer_text: 'CARTO · Made in Madrid & New York City since 2012'
      support_link: 'mailto:support@carto.com'
      include_carto_links: true
  varnish_management:
    critical: false
    host: '127.0.0.1'
    port: 6082
    http_port: 6081
    purge_command: 'purge'
    retries: 5
    timeout: 5
    # 'warning' or 'error'
    trigger_verbose: true
  invalidation_service:
    enabled: false
    host: '127.0.0.1'
    port: 3142
    retries: 5 # number of retries before considering failure
    critical: false # either the failure is considered an error or a warning
    timeout: 5 # socket timeout
    trigger_verbose: true
  redis:
    host: '127.0.0.1'
    port: 6379
    connect_timeout: 2
    read_timeout: 3
    write_timeout: 5
    databases:
      tables_metadata:     0
      api_credentials:     3
      users_metadata:      5
      redis_migrator_logs: 6
      limits_metadata:     8
    # secondary:
    #   host: '127.0.0.1'
  org_metadata_api:
    host: 'localhost.lan'
    port: '3000'
    username: "extension"
    password: "elephant"
    timeout: 10
  superadmin:
    username: "superadmin"
    password: "monkey"
  geocoder:
    #force_batch: true
    #disable_cache: true
    app_id: ''
    token:  ''
    mailto: ''
    base_url: ''
    non_batch_base_url: ''
    internal:
      username: ''
      api_key: ''
    cache:
      base_url: ''
      api_key: ''
      table_name: ''
    search_bar_provider: ''
    mapbox:
      search_bar_api_key: ''
    tomtom:
      search_bar_api_key: ''
    api:
      host: 'localhost'
      port: '5432'
      dbname: 'dataservices_db'
      user: 'geocoder_api'
  user_migrator:
    user_exports_folder: '/tmp/user_exports'
    user_imports_folder: '/tmp/user_imports'
    s3:
      access_key_id: ''
      secret_access_key: ''
      bucket_name: ''
      url_ttl: 7200
      async_long_uploads: false
      region: ''
    uploads_path: 'public/uploads'
    pg_dump_bin_path:
      '9.5': 'pg_dump'
      '10': 'pg_dump'
    pg_restore_bin_path:
      '9.5': 'pg_restore'
      '10': 'pg_restore'
  exporter:
    exporter_temporal_folder: '/tmp/exporter'
    s3:
      access_key_id: ''
      secret_access_key: ''
      bucket_name: ''
      url_ttl: 7200
      async_long_uploads: false
      s3_endpoint: ''
      region: ''
    uploads_path: 'public/uploads' # including 'uploads' assumes public path. Absolute path example: /tmp/exports/downloads
    python_bin_path: '/usr/bin/python3'
  importer:
    python_bin_path: '/usr/bin/python3'
    blacklisted_ip_addr: []
    content_guessing:        # Depends on geocoding
      enabled:         false # Disabled if false or not present
      threshold:       0.9   # 90% or more matches
      minimum_entropy: 0.9   # Normalized entropy, between 0.0 and 1.0. See http://en.wikipedia.org/wiki/Entropy_(information_theory)
      sample_size:     400   # +-5% error. See http://en.wikipedia.org/wiki/Sample_size_determination#Estimating_proportions_and_means
    s3:
      access_key_id:
      secret_access_key:
      bucket_name:
      url_ttl:
      async_long_uploads: false
      proxy_uri:
      s3_endpoint: '' # :use_ssl has been removed. Version 2 uses SSL everywhere. To disable SSL you must configure an :endpoint that uses http://.
      region: ''

    unp_temporal_folder: '/tmp/imports/'
    # It must end in `/uploads` and be accessible via HTTP, if relative will default to Rails.Root/#{uploads_path}
    uploads_path: 'public/uploads'
  error_track:
    url: 'https://viz2.carto.com/api/v1/sql'
    percent_users: 10
  # graphite endpoint used to post frontend stats
  graphite_public:
    host: ""
    port:
  layer_opts:
    public_opts: ["type", "active", "query", "opacity", "auto_bound",
                  "interactivity", "debug", "visible", "tiler_domain",
                  "tiler_port", "tiler_protocol", "sql_domain", "sql_port",
                  "sql_protocol", "extra_params", "table_name",
                  "user_name", "style_version", "tile_style", "query_wrapper"]
    default_tile_styles:
      point: "{\n  marker-fill: #FF6600;\n  marker-opacity: 0.9;\n  marker-width: 12;\n  marker-line-color: white;\n  marker-line-width: 3;\n  marker-line-opacity: 0.9;\n  marker-placement: point;\n  marker-type: ellipse;\n  marker-allow-overlap: true;\n}"
      geometry: "{\n // points\n [mapnik-geometry-type=point] {\n    marker-fill: #FF6600;\n    marker-opacity: 1;\n    marker-width: 12;\n    marker-line-color: white;\n    marker-line-width: 3;\n    marker-line-opacity: 0.9;\n    marker-placement: point;\n    marker-type: ellipse;marker-allow-overlap: true;\n  }\n\n //lines\n [mapnik-geometry-type=linestring] {\n    line-color: #FF6600; \n    line-width: 2; \n    line-opacity: 0.7;\n  }\n\n //polygons\n [mapnik-geometry-type=polygon] {\n    polygon-fill:#FF6600;\n    polygon-opacity: 0.7;\n    line-opacity:1;\n    line-color: #FFFFFF;\n   }\n }"
      polygon: "{\n  polygon-fill:#FF6600;\n  polygon-opacity: 0.7;\n  line-opacity:1;\n  line-color: #FFFFFF;\n}"
      multipolygon: "{\n  polygon-fill:#FF6600;\n  polygon-opacity: 0.7;\n  line-opacity:1;\n  line-color: #FFFFFF;\n}"
      multilinestring: "{\n  line-color:#FF6600;\n  line-width:1;\n  line-opacity: 0.7;\n}"
    data:
      kind: "carto"
      options:
        # attribution:        'CARTO attribution'
        query:              ""
        opacity:            0.99
        auto_bound:         false
        interactivity:      "cartodb_id"
        debug:              false
        visible:            true
        tiler_domain:       "localhost.lan"
        tiler_port:         "80"
        tiler_protocol:     "http"
        sql_domain:         "localhost.lan"
        sql_port:           "80"
        sql_protocol:       "http"
        extra_params:       { cache_policy: 'persist' }
        tile_style_history: []
        style_version:      "2.1.1"
      infowindow:
        template_name:      "table/views/infowindow_light"
    background:
      kind: "background"
      options: { color: '#ffffff' }
  cartodb_com_hosted: true
  cartodb_central_domain_name: 'carto.com'
  #aws:
    #s3:
      #access_key_id: "test"
      #secret_access_key: "test"
      #region: ''
  assets:
    s3_bucket_name: "tests"
    max_file_size: 5242880 # 5.megabytes
    region: ''
    # Example for configuring organization assets.
    # If 'aws.s3' configuration exists, S3 is used for storing assets and 'assets.organization.bucket' value is required. If 'aws.s3' config is not present, assets will be stored locally.
    # organization:
    #   bucket: "tests" # Required if 'aws.s3' config is present. Bucket must exist beforehand. If no 'aws.s3' config is present, organization assets will be stored locally and this line is not needed.
    #   max_size_in_bytes: 1048576 # Optional, default is 1 MB
    #   location: 'organization_assets' # Optional subdirectory for local assets, default is 'organization_assets'
    # html:
    #   bucket: "tests" # Required if 'aws.s3' config is present. Bucket must exist beforehand. If no 'aws.s3' config is present, html assets will be stored locally and this line is not needed.
    #   max_size_in_bytes: 1048576 # Optional, default is 1 MB
    #   location: 'html_assets' # Optional subdirectory for local assets, default is 'html_assets'
  app_assets:
    asset_host: "//cartodb-libs.global.ssl.fastly.net/cartodbui"
  avatars:
    gravatar_enabled: true
    base_url: '/assets/unversioned/images/avatars'
    kinds: ['ghost', 'heart', 'marker', 'mountain', 'pacman', 'planet', 'star']
    colors: ['green', 'orange', 'red', 'yellow']
  dropbox_api_key: ""
  gdrive:
    api_key: ""
    app_id: ""
  # This enables a support chat within editor
  # Use your Olark api id to enable it. If you remove this entry or don't define an app key, it won't be activated.
  olark:
    app_id: ''
  enforce_non_empty_layer_css: true
  users_dumps:
    service:
      port: 00000
  http_header_authentication:
    header: # name of the trusted, safe header that your server adds to the request
    field: # 'email' / 'username' / 'id' / 'auto' (autodetection)
    autocreation: # true / false (true requires field to be email)
  oauth:
    # If the client_id/app_key is not set won't appear at the UI. @see application_helper.rb -> frontend_config
    # Must be the same as CartoDB::Datasources::xxxx DATASOURCE_NAME constants
    bigquery:
      application_name: ''
      client_id: ''
      client_secret: ''
      scope: ["https://www.googleapis.com/auth/bigquery"]
      authorization_uri: "https://accounts.google.com/o/oauth2/auth"
      revoke_auth_uri: "https://accounts.google.com/o/oauth2/revoke"
      token_credential_uri: "https://oauth2.googleapis.com/token"
      callback_url: "https://oauth.carto-staging.com"
    gdrive:
      application_name:     ''
      client_id:            ''
      client_secret:        ''
      callback_url:         'https://carto.com'
    # google_plus:
      # client_id: ''
      # client_secret: ''
      # cookie_policy: 'single_host_origin'
      # cookie_policy: 'https://cartodb-staging.com'
    github:
      client_id:            ''
      client_secret:        ''
    dropbox:
      app_key:              ''
      app_secret:           ''
      callback_url:         ''
    box:
      application_name:     ''
      client_id:            ''
      client_secret:        ''
      box_host:             "app.box.com"
    instagram:
      app_key:              ''
      app_secret:           ''
      callback_url:         ''
    # Mailchimp datasource. Setup at https://admin.mailchimp.com/account/oauth2/ then fill here.
    # If fields are present but empty, option won't appear at editor import window
    mailchimp:
      app_key:              ''
      app_secret:           ''
      callback_url:         ''
  datasource_search:
    # Must be the same as CartoDB::Datasources::xxxx DATASOURCE_NAME constants
    twitter_search:
      standard:
        auth_required:          false
        username:               ''
        password:               ''
        search_url:             'http://fake.url.nil'
        ratelimit_active:       true
        ratelimit_concurrency:  8
        ratelimit_ttl:          4
        ratelimit_wait_secs:    0.5
      customized_user_list:     []
      customized_orgs_list:     []
      entity_to_config_map:     [] # { user_or_org_name: 'custom_config_name'}
      customized:
        custom1:
            auth_required:          false
            username:               ''
            password:               ''
            search_url:             'http://fake.url.nil'
            ratelimit_active:       false
            ratelimit_concurrency:  3
            ratelimit_ttl:          4
            ratelimit_wait_secs:    0.1
  datasources:
    arcgis_enabled: false
    salesforce_enabled: false
  basemaps: # Adding `default: true` at a basemap marks its group as the default one. Its first basemap becomes the default one.
    CARTO:
      voyager_labels:
        default: true
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Voyager'
        className: 'voyager_labels'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
        labels:
          urlTemplate: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}.png'
          urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_only_labels/{z}/{x}/{y}@2x.png'
      positron_rainbow_labels:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Positron'
        className: 'positron_rainbow_labels'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
        labels:
          urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}.png'
          urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}@2x.png'
      dark_matter_rainbow_labels:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Dark matter'
        className: 'dark_matter_rainbow_labels'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
        labels:
          urlTemplate: 'https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}.png'
          urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/dark_only_labels/{z}/{x}/{y}@2x.png'
      voyager:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Voyager (labels below)'
        className: 'voyager'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      positron_rainbow:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Positron (labels below)'
        className: 'positron_rainbow'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      dark_matter_rainbow:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Dark matter (labels below)'
        className: 'dark_matter_rainbow'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      voyager_lite:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Voyager (lite)'
        className: 'voyager_lite'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      positron_lite_rainbow:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Positron (lite)'
        className: 'positron_lite_rainbow'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      dark_matter_lite_rainbow:
        urlTemplate: 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}.png'
        urlTemplate2x: 'https://{s}.basemaps.cartocdn.com/dark_nolabels/{z}/{x}/{y}@2x.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Dark matter (lite)'
        className: 'dark_matter_lite_rainbow'
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors © <a href="https://carto.com/attributions/">CARTO</a>'
      eco_cartodb:
        urlTemplate: 'https://cartocdn_{s}.global.ssl.fastly.net/base-eco/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '10'
        name: 'CARTO World Eco'
        className: 'eco_cartodb'
        attribution: ''
      flat_blue:
        urlTemplate: 'https://cartocdn_{s}.global.ssl.fastly.net/base-flatblue/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '10'
        name: 'CARTO World Flat Blue'
        className: 'flat_blue'
        attribution: ''
      midnight_cartodb:
        urlTemplate: 'https://cartocdn_{s}.global.ssl.fastly.net/base-midnight/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '10'
        name: 'CARTO World Midnight Commander'
        className: 'midnight_cartodb'
        attribution: ''
      antique_cartodb:
        urlTemplate: 'https://cartocdn_{s}.global.ssl.fastly.net/base-antique/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: 0
        maxZoom: 10
        name: 'CARTO World Antique'
        className: 'antique_cartodb'
        attribution: ''
    Stamen:
      toner_stamen_labels:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner'
        className: 'toner_stamen_labels'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
        labels:
          urlTemplate: 'http://{s}.tile.stamen.com/toner-labels/{z}/{x}/{y}.png'
      toner_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner (labels below)'
        className: 'toner_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
      toner_background_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-background/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner Background'
        className: 'toner_background_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
      toner_lite_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner Lite'
        className: 'toner_lite_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
      toner_lines_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lines/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner Lines'
        className: 'toner_lines_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
      toner_hybrid_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Toner Hybrid'
        className: 'toner_hybrid_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
      watercolor_stamen:
        urlTemplate: 'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.png'
        subdomains: 'abcd'
        minZoom: '0'
        maxZoom: '18'
        name: 'Watercolor'
        className: 'watercolor_stamen'
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
    GMaps:
      roadmap:
        name: 'GMaps Roadmap'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        className: 'googlemaps'
        style: '[]'
        default: true
      hybrid:
        name: 'GMaps Hybrid'
        maxZoom: 40
        minZoom: 0
        baseType: 'hybrid'
        className: 'googlemaps'
        style: '[]'
      satellite:
        name: 'GMaps Satellite'
        maxZoom: 40
        minZoom: 0
        baseType: 'satellite'
        className: 'googlemaps'
        style: '[]'
      terrain:
        name: 'GMaps Terrain'
        maxZoom: 40
        minZoom: 0
        baseType: 'terrain'
        className: 'googlemaps'
        style: '[]'
      gray_roadmap:
        name: 'GMaps Gray Roadmap'
        maxZoom: 40
        minZoom: 0
        baseType: 'gray_roadmap'
        className: 'googlemaps'
        style: '[{ "stylers": [ { "saturation": -100 } ] },{ "featureType": "water", "stylers": [ { "gamma": 1.67 }, { "lightness": 27 } ] },{ "elementType": "geometry", "stylers": [ { "gamma": 1.31 }, { "lightness": 12 } ] },{ "featureType": "administrative", "elementType": "labels", "stylers": [ { "lightness": 51 }, { "gamma": 0.94 } ] },{ },{ "featureType": "road", "elementType": "labels", "stylers": [ { "lightness": 57 } ] },{ "featureType": "poi", "elementType": "labels", "stylers": [ { "lightness": 42 } ] }]'
      cool_grey:
        name: 'GMaps cool grey'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'cool_grey'
        className: 'googlemaps'
        style: '[{"featureType":"landscape","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"water","stylers":[{"visibility":"on"},{"color":"#ffffff"}]},{"featureType":"road","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"stylers":[{"hue":"#00aaff"},{"saturation":-100},{"gamma":2.15},{"lightness":12}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"visibility":"on"},{"lightness":24}]},{"featureType":"road","elementType":"geometry","stylers":[{"lightness":57}]}]'
      clean_grey:
        name: 'GMaps clean grey'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'clean_grey'
        className: 'googlemaps'
        style: '[{"featureType":"administrative","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"administrative.country","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"administrative.province","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"visibility":"on"},{"color":"#e3e3e3"}]},{"featureType":"landscape.natural","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"all","stylers":[{"color":"#cccccc"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"transit.line","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"transit.line","elementType":"labels.text","stylers":[{"visibility":"off"}]},{"featureType":"transit.station.airport","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"transit.station.airport","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#FFFFFF"}]},{"featureType":"water","elementType":"labels","stylers":[{"visibility":"off"}]}]'
      shades_grey:
        name: 'GMaps shades of grey'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'shades_grey'
        className: 'googlemaps'
        style: '[{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#000000"},{"lightness":40}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#000000"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":17},{"weight":1.2}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":21}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":17}]}]'
      neutral_blue:
        name: 'GMaps neutral blue'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'neutral_blue'
        className: 'googlemaps'
        style: '[{"featureType":"water","elementType":"geometry","stylers":[{"color":"#193341"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#2c5a71"}]},{"featureType":"road","elementType":"geometry","stylers":[{"color":"#29768a"},{"lightness":-37}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#406d80"}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#406d80"}]},{"elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#3e606f"},{"weight":2},{"gamma":0.84}]},{"elementType":"labels.text.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"administrative","elementType":"geometry","stylers":[{"weight":0.6},{"color":"#1a3541"}]},{"elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#2c5a71"}]}]'
      cleaner_midnight:
        name: 'GMaps cleaner midnight'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'cleaner_midnight'
        className: 'googlemaps'
        style: '[{"featureType":"all","elementType":"labels.text.fill","stylers":[{"color":"#ffffff"},{"weight":"0.20"},{"lightness":"28"},{"saturation":"23"},{"visibility":"off"}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"color":"#494949"},{"lightness":13},{"visibility":"off"}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#144b53"},{"lightness":14},{"weight":1.4}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#08304b"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#0c4152"},{"lightness":5}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#000000"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#0b434f"},{"lightness":25}]},{"featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#000000"}]},{"featureType":"road.arterial","elementType":"geometry.stroke","stylers":[{"color":"#0b3d51"},{"lightness":16}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"}]},{"featureType":"transit","elementType":"all","stylers":[{"color":"#146474"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#021019"}]}]'
      icy_blue:
        name: 'GMaps icy blue'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'icy_blue'
        className: 'googlemaps'
        style: '[{"stylers":[{"hue":"#2c3e50"},{"saturation":250}]},{"featureType":"road","elementType":"geometry","stylers":[{"lightness":50},{"visibility":"simplified"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]}]'
      red_hues:
        name: 'GMaps red hues'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'red_hues'
        className: 'googlemaps'
        style: '[{"stylers":[{"hue":"#dd0d0d"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"geometry","stylers":[{"lightness":100},{"visibility":"simplified"}]}]'
      light_green:
        name: 'GMaps light green'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'light_green'
        className: 'googlemaps'
        style: '[{"stylers":[{"hue":"#baf4c4"},{"saturation":10}]},{"featureType":"water","stylers":[{"color":"#effefd"}]},{"featureType":"all","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"labels","stylers":[{"visibility":"on"}]},{"featureType":"road","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]}]'
      mostly_grayscale:
        name: 'GMaps mostly grayscale'
        maxZoom: 40
        minZoom: 0
        baseType: 'roadmap'
        baseName: 'mostly_grayscale'
        className: 'googlemaps'
        style: '[{"featureType":"administrative","elementType":"all","stylers":[{"visibility":"on"},{"lightness":33}]},{"featureType":"administrative","elementType":"labels","stylers":[{"saturation":"-100"}]},{"featureType":"administrative","elementType":"labels.text","stylers":[{"gamma":"0.75"}]},{"featureType":"administrative.neighborhood","elementType":"labels.text.fill","stylers":[{"lightness":"-37"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#f9f9f9"}]},{"featureType":"landscape.man_made","elementType":"geometry","stylers":[{"saturation":"-100"},{"lightness":"40"},{"visibility":"off"}]},{"featureType":"landscape.natural","elementType":"labels.text.fill","stylers":[{"saturation":"-100"},{"lightness":"-37"}]},{"featureType":"landscape.natural","elementType":"labels.text.stroke","stylers":[{"saturation":"-100"},{"lightness":"100"},{"weight":"2"}]},{"featureType":"landscape.natural","elementType":"labels.icon","stylers":[{"saturation":"-100"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"saturation":"-100"},{"lightness":"80"}]},{"featureType":"poi","elementType":"labels","stylers":[{"saturation":"-100"},{"lightness":"0"}]},{"featureType":"poi.attraction","elementType":"geometry","stylers":[{"lightness":"-4"},{"saturation":"-100"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#c5dac6"},{"visibility":"on"},{"saturation":"-95"},{"lightness":"62"}]},{"featureType":"poi.park","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"lightness":20}]},{"featureType":"road","elementType":"labels","stylers":[{"saturation":"-100"},{"gamma":"1.00"}]},{"featureType":"road","elementType":"labels.text","stylers":[{"gamma":"0.50"}]},{"featureType":"road","elementType":"labels.icon","stylers":[{"saturation":"-100"},{"gamma":"0.50"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#c5c6c6"},{"saturation":"-100"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"lightness":"-13"}]},{"featureType":"road.highway","elementType":"labels.icon","stylers":[{"lightness":"0"},{"gamma":"1.09"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#e4d7c6"},{"saturation":"-100"},{"lightness":"47"}]},{"featureType":"road.arterial","elementType":"geometry.stroke","stylers":[{"lightness":"-12"}]},{"featureType":"road.arterial","elementType":"labels.icon","stylers":[{"saturation":"-100"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#fbfaf7"},{"lightness":"77"}]},{"featureType":"road.local","elementType":"geometry.fill","stylers":[{"lightness":"-5"},{"saturation":"-100"}]},{"featureType":"road.local","elementType":"geometry.stroke","stylers":[{"saturation":"-100"},{"lightness":"-15"}]},{"featureType":"transit.station.airport","elementType":"geometry","stylers":[{"lightness":"47"},{"saturation":"-100"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"color":"#acbcc9"}]},{"featureType":"water","elementType":"geometry","stylers":[{"saturation":"53"}]},{"featureType":"water","elementType":"labels.text.fill","stylers":[{"lightness":"-42"},{"saturation":"17"}]},{"featureType":"water","elementType":"labels.text.stroke","stylers":[{"lightness":"61"}]}]'
  overviews:
    min_rows: 2000000
    statement_timeout: 1800000
    tolerance_px: 1.0
  connectors:
    odbc:
      enabled: false
      max_rows: nil
    mysql:
      enabled: true
      max_rows: 500000
    postgresql:
      enabled: true
      max_rows: 500000
    hive:
      enabled: false
      max_rows: 500000
    sqlserver:
      enabled: false
      max_rows: 500000
    bigquery:
      enabled: false
      max_rows: 1000000
  enforce_non_empty_layer_css: false
  dataservices:
    enabled:
        geocoder_internal: false
        hires_geocoder: false
        isolines: false
        routing: false
        data_observatory: false
  disable_email_mx_check: false # Disables MX DNS record check and just performs syntax validation.
  dbdirect:
    certificates:
      ca_arn: "arn:aws:acm-pca:zzzzzz:XXXXXXXXXXX:certificate-authority/XXXXXXXXXXXXXXXX"
      maximum_validity_days: 365
      aws_access_key_id: ''
      aws_secret_key: ''
      aws_region: us-east-1
    pgproxy:
      host: 'dbconn.carto.com'
      port: 5432
    firewall:
      enabled: false
      project_id: ''
      rule_name: ''
      network: ''
      target_tag: ''
      ports: 'tcp:5432'

development:
  <<: *defaults
  http_port: 3000
  varnish_management:
    critical: false
    host: '127.0.0.1'
    port: 6082
    purge_command: 'purge'
    url_purge_command: 'url.purge'
    retries: 5
    timeout: 5
  varnish_management:
    critical: false
    host: '127.0.0.1'
    port: 6082
    http_port: 6081
    purge_command: 'purge'
    retries: 1
    timeout: 1
    # 'warning' or 'error'
    trigger_verbose: false
  invalidation_service:
    enabled: false
    host: '127.0.0.1'
    port: 3142
    retries: 1 # number of retries before considering failure
    critical: false # either the failure is considered an error or a warning
    timeout: 1 # socket timeout
    trigger_verbose: false
  do_metadata_database:
    host: 'localhost'
    port: 5432
    database: 'catalog'
    username: ''
    password: ''

test:
  <<: *defaults
  http_port: 53716
  redis:
    host: '127.0.0.1'
    port: 6335
  enforce_non_empty_layer_css: false
  api_requests_es_service:
    url: "http://api-calls-service.localhost.lan/search"
    body: ""
  session_domain:     '.localhost.lan'
  subdomainless_urls: false
  federated_server:
    dir: "/tmp/federated_server_db"
    port: 22665
    test_user: "remote_user"
  varnish_management:
    critical: false
    host: '127.0.0.1'
    port: 6082
    http_port: 6081
    purge_command: 'purge'
    retries: 1
    timeout: 1
    # 'warning' or 'error'
    trigger_verbose: false
  invalidation_service:
    enabled: false
    host: '127.0.0.1'
    port: 3142
    retries: 1 # number of retries before considering failure
    critical: false # either the failure is considered an error or a warning
    timeout: 1 # socket timeout
    trigger_verbose: false
  do_metadata_database:
    host: 'localhost'
    port: 5432
    database: 'carto_db_test'
    username: 'postgres'
    password: ''

staging:
  <<: *defaults

production:
  <<: *defaults
