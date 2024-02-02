from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options

# Configuration for iOS tests
ios_capabilities = XCUITestOptions()
ios_capabilities.platform_name = 'iOS'
ios_capabilities.automation_name = 'XCUITest'
ios_capabilities.device_name = 'Martin iPad'  # Your device name
ios_capabilities.platform_version = '16.4'   # Your platform version
ios_capabilities.bundle_id = 'com.dpolyakov.expoffmpegkitexample'

# Configuration for Android tests
android_capabilities = UiAutomator2Options()
android_capabilities.platform_name = 'Android'
android_capabilities.automation_name = 'UiAutomator2'
android_capabilities.device_name = 'emulator-5554'  # Your device name
#android_capabilities.app_package = 'com.android.settings'  
#android_capabilities.app_activity = '.Settings' 
android_capabilities.app_package = 'ssf.io'  
android_capabilities.app_activity = 'ssf_expo_router' 