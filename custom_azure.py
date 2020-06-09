from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'socialite' # Must be replaced by your <storage_account_name>
    account_key = '7GEqXX920J+TuMGojSq+tGUXeFIyPp0CJgzAkWnNecTlWLyWwhpkHARnaFp0aCI+R/XJrszzB4NgAVGMMCv/rg==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'socialite' # Must be replaced by your storage_account_name
    account_key = '7GEqXX920J+TuMGojSq+tGUXeFIyPp0CJgzAkWnNecTlWLyWwhpkHARnaFp0aCI+R/XJrszzB4NgAVGMMCv/rg==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None