from regression_tests import *

class TestNewARM32Signatures(Test):
    settings = TestSettings(
        input='arm.exe'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('__security_check_cookie', 0x401000)
        assert self.out_config.is_statically_linked('memset', 0x401040)
        assert self.out_config.is_statically_linked('memcmp', 0x401bdc)
        assert self.out_config.is_statically_linked('__scrt_acquire_startup_lock', 0x401eec)
        assert self.out_config.is_statically_linked('__scrt_release_startup_lock', 0x402078)
        assert self.out_config.is_statically_linked('_onexit', 0x4020d4)
        assert self.out_config.is_statically_linked('__security_init_cookie', 0x40212c)
        assert self.out_config.is_statically_linked('__scrt_is_user_matherr_present', 0x402240)
        assert self.out_config.is_statically_linked('_RTC_Initialize', 0x402340)
        assert self.out_config.is_statically_linked('__vcrt_freefls', 0x4025e4)
        assert self.out_config.is_statically_linked('__vcrt_initialize_ptd', 0x402604)
        assert self.out_config.is_statically_linked('__vcrt_uninitialize_ptd', 0x40264c)
        assert self.out_config.is_statically_linked('__vcrt_initialize_locks', 0x402678)
        assert self.out_config.is_statically_linked('__acrt_uninitialize_locks', 0x4026c0)
        assert self.out_config.is_statically_linked('__vcrt_initialize_pure_virtual_call_handler', 0x402704)
        assert self.out_config.is_statically_linked('__acrt_initialize_stdio', 0x402730)
        assert self.out_config.is_statically_linked('__acrt_iob_func', 0x4027dc)
        assert self.out_config.is_statically_linked('_lock_file', 0x40283c)
        assert self.out_config.is_statically_linked('_unlock_file', 0x402854)
        assert self.out_config.is_statically_linked('__acrt_has_user_matherr', 0x403bc8)
        assert self.out_config.is_statically_linked('__setusermatherr', 0x403c34)
        assert self.out_config.is_statically_linked('__dcrt_uninitialize_environments_nolock', 0x4041bc)
        assert self.out_config.is_statically_linked('_register_thread_local_exe_atexit_callback', 0x4044c8)
        assert self.out_config.is_statically_linked('__acrt_initialize_command_line', 0x404564)
        assert self.out_config.is_statically_linked('__acrt_set_locale_changed', 0x4045b4)
        assert self.out_config.is_statically_linked('_initialize_onexit_table', 0x40498c)
        assert self.out_config.is_statically_linked('initialize_global_variables', 0x4049f8)
        assert self.out_config.is_statically_linked('initialize_c', 0x404a14)
        assert self.out_config.is_statically_linked('_free_base', 0x404b78)
        assert self.out_config.is_statically_linked('__doserrno', 0x4050c0)
        assert self.out_config.is_statically_linked('_errno', 0x4050dc)
        assert self.out_config.is_statically_linked('__acrt_uninitialize_lowio', 0x4059f0)
        assert self.out_config.is_statically_linked('__acrt_uninitialize_ptd', 0x406260)
        assert self.out_config.is_statically_linked('_get_printf_count_output', 0x406c54)
        assert self.out_config.is_statically_linked('__acrt_lowio_destroy_handle_array', 0x407dbc)
        assert self.out_config.is_statically_linked('__acrt_lowio_lock_fh', 0x407e64)
        assert self.out_config.is_statically_linked('_free_osfhnd', 0x407ec4)
        assert self.out_config.is_statically_linked('__acrt_locale_free_monetary', 0x407ff0)
        assert self.out_config.is_statically_linked('__acrt_locale_free_numeric', 0x4080a4)
        assert self.out_config.is_statically_linked('__acrt_add_locale_ref', 0x408314)
        assert self.out_config.is_statically_linked('__acrt_locale_add_lc_time_reference', 0x4084f4)
        assert self.out_config.is_statically_linked('__acrt_locale_release_lc_time_reference', 0x40855c)
        assert self.out_config.is_statically_linked('__acrt_release_locale_ref', 0x408594)
        assert self.out_config.is_statically_linked('__acrt_uninitialize_heap', 0x4087c0)
        assert self.out_config.is_statically_linked('_query_new_handler', 0x40887c)
        assert self.out_config.is_statically_linked('__acrt_initialize_signal_handlers', 0x40895c)
        assert self.out_config.is_statically_linked('__acrt_DownlevelLocaleNameToLCID', 0x408c04)
        assert self.out_config.is_statically_linked('_isatty', 0x40ac78)
        assert self.out_config.is_statically_linked('_msize_base', 0x40b154)
        assert self.out_config.is_statically_linked('_close_nolock', 0x40b308)
        assert self.out_config.is_statically_linked('_putwch_nolock', 0x40b58c)
        assert self.out_config.is_statically_linked('__strncnt', 0x40b5dc)
        assert self.out_config.is_statically_linked('log10', 0x40b74c)
        assert self.out_config.is_statically_linked('__ascii_strnicmp', 0x40ba40)
        assert self.out_config.is_statically_linked('__dcrt_lowio_initialize_console_output', 0x40be50)
        assert self.out_config.is_statically_linked('__get_machine_status', 0x40beb4)
        assert self.out_config.is_statically_linked('_abstract_cw', 0x40bf5c)
        assert self.out_config.is_statically_linked('_abstract_sw', 0x40bff0)
        assert self.out_config.is_statically_linked('_hw_cw', 0x40c0c4)
        assert self.out_config.is_statically_linked('_ctrlfp', 0x40c674)
        assert self.out_config.is_statically_linked('_FindPESection', 0x40c6e4)
        assert self.out_config.is_statically_linked('_ValidateImageBase', 0x40c76c)
        assert self.out_config.is_statically_linked('strrchr', 0x40c7c4)
        assert self.out_config.is_statically_linked('strchr', 0x40c7f8)

class TestNewx86Signatures(Test):
    settings = TestSettings(
        input='x86.exe'
    )

    def test_check_correct_static_functions_detection(self):
        assert self.out_config.is_statically_linked('___raise_securityfailure', 0x401298)
        assert self.out_config.is_statically_linked('___report_gsfailure', 0x4012c0)
        assert self.out_config.is_statically_linked('___scrt_acquire_startup_lock', 0x4013ff)
        assert self.out_config.is_statically_linked('___scrt_initialize_crt', 0x401434)
        assert self.out_config.is_statically_linked('___scrt_initialize_onexit_tables', 0x40146d)
        assert self.out_config.is_statically_linked('___scrt_is_nonwritable_in_current_image', 0x401504)
        assert self.out_config.is_statically_linked('___scrt_release_startup_lock', 0x40158e)
        assert self.out_config.is_statically_linked('___scrt_uninitialize_crt', 0x4015ab)
        assert self.out_config.is_statically_linked('__onexit', 0x4015d3)
        assert self.out_config.is_statically_linked('_atexit', 0x40160e)
        assert self.out_config.is_statically_linked('___security_init_cookie', 0x401623)
        assert self.out_config.is_statically_linked('__initialize_default_precision', 0x4016d5)
        assert self.out_config.is_statically_linked('___scrt_fastfail', 0x401732)
        assert self.out_config.is_statically_linked('__SEH_prolog4', 0x401910)
        assert self.out_config.is_statically_linked('__SEH_epilog4', 0x401956)
        assert self.out_config.is_statically_linked('___isa_available_init', 0x40196b)
        assert self.out_config.is_statically_linked('_ValidateLocalCookies', 0x401b20)
        assert self.out_config.is_statically_linked('__except_handler4', 0x401b60)
        assert self.out_config.is_statically_linked('___vcrt_initialize', 0x401cc6)
        assert self.out_config.is_statically_linked('___vcrt_uninitialize', 0x401cef)
        assert self.out_config.is_statically_linked('_memset', 0x401d10)
        assert self.out_config.is_statically_linked('__local_unwind4', 0x401e70)
        assert self.out_config.is_statically_linked('__unwind_handler4', 0x401f00)
        assert self.out_config.is_statically_linked('___vcrt_initialize_ptd', 0x401fea)
        assert self.out_config.is_statically_linked('___vcrt_uninitialize_ptd', 0x40201d)
        assert self.out_config.is_statically_linked('___vcrt_initialize_locks', 0x402038)
        assert self.out_config.is_statically_linked('___vcrt_uninitialize_locks', 0x402074)
        assert self.out_config.is_statically_linked('___vcrt_FlsAlloc', 0x4021e1)
        assert self.out_config.is_statically_linked('___vcrt_FlsFree', 0x40221b)
        assert self.out_config.is_statically_linked('___vcrt_FlsSetValue', 0x402255)
        assert self.out_config.is_statically_linked('___vcrt_InitializeCriticalSectionEx', 0x402292)
        assert self.out_config.is_statically_linked('___vcrt_initialize_winapi_thunks', 0x4022d8)
        assert self.out_config.is_statically_linked('___vcrt_uninitialize_winapi_thunks', 0x402312)
        assert self.out_config.is_statically_linked('___vcrt_initialize_pure_virtual_call_handler', 0x402344)
        assert self.out_config.is_statically_linked('__global_unwind2', 0x402370)
        assert self.out_config.is_statically_linked('__unwind_handler', 0x402390)
        assert self.out_config.is_statically_linked('__local_unwind2', 0x4023d5)
        assert self.out_config.is_statically_linked('__abnormal_termination', 0x402459)
        assert self.out_config.is_statically_linked('__NLG_Notify', 0x402485)
        assert self.out_config.is_statically_linked('___acrt_initialize_stdio', 0x4024a7)
        assert self.out_config.is_statically_linked('___acrt_iob_func', 0x40256f)
        assert self.out_config.is_statically_linked('___acrt_uninitialize_stdio', 0x40257f)
        assert self.out_config.is_statically_linked('__lock_file', 0x4025cb)
        assert self.out_config.is_statically_linked('__unlock_file', 0x4025df)
        assert self.out_config.is_statically_linked('__seh_filter_exe', 0x40398f)
        assert self.out_config.is_statically_linked('___acrt_has_user_matherr', 0x403b48)
        assert self.out_config.is_statically_linked('___acrt_initialize_new_handler', 0x403b61)
        assert self.out_config.is_statically_linked('___acrt_invoke_user_matherr', 0x403b75)
        assert self.out_config.is_statically_linked('___setusermatherr', 0x403bbe)
        assert self.out_config.is_statically_linked('___acrt_allocate_buffer_for_argv', 0x403e6c)
        assert self.out_config.is_statically_linked('___dcrt_uninitialize_environments_nolock', 0x40414e)
        #assert self.out_config.is_statically_linked('__get_initial_wide_environment', 0x404185)
        assert self.out_config.is_statically_linked('__initterm', 0x40419e)
        assert self.out_config.is_statically_linked('__initterm_e', 0x4041fa)
        assert self.out_config.is_statically_linked('__Exit', 0x404487)
        assert self.out_config.is_statically_linked('__register_thread_local_exe_atexit_callback', 0x40449d)
        assert self.out_config.is_statically_linked('_exit', 0x4044d5)
        assert self.out_config.is_statically_linked('__set_fmode', 0x4044eb)
        assert self.out_config.is_statically_linked('___acrt_initialize_command_line', 0x404528)
        assert self.out_config.is_statically_linked('__configthreadlocale', 0x4045aa)
        assert self.out_config.is_statically_linked('__set_new_mode', 0x404612)
        assert self.out_config.is_statically_linked('__crt_atexit', 0x4049b9)
        assert self.out_config.is_statically_linked('__initialize_onexit_table', 0x4049ec)
        assert self.out_config.is_statically_linked('__register_onexit_function', 0x404a29)
        assert self.out_config.is_statically_linked('_initialize_global_variables', 0x404a4d)
        assert self.out_config.is_statically_linked('_initialize_c', 0x404a5f)
        assert self.out_config.is_statically_linked('_initialize_pointers', 0x404a84)
        assert self.out_config.is_statically_linked('__controlfp_s', 0x404b65)
        assert self.out_config.is_statically_linked('_terminate', 0x404bc4)
        assert self.out_config.is_statically_linked('__free_base', 0x404c00)
        assert self.out_config.is_statically_linked('__malloc_base', 0x404c3a)
        assert self.out_config.is_statically_linked('_strcpy_s', 0x404c88)
        assert self.out_config.is_statically_linked('_abort', 0x404ce2)
        assert self.out_config.is_statically_linked('__calloc_base', 0x404d25)
        assert self.out_config.is_statically_linked('__chvalidchk_l', 0x405020)
        assert self.out_config.is_statically_linked('__ischartype_l', 0x40504a)
        assert self.out_config.is_statically_linked('___acrt_call_reportfault', 0x40507d)
        assert self.out_config.is_statically_linked('__invalid_parameter', 0x4051cc)
        assert self.out_config.is_statically_linked('__invalid_parameter_noinfo', 0x405247)
        assert self.out_config.is_statically_linked('__invoke_watson', 0x405257)
        assert self.out_config.is_statically_linked('___acrt_errno_map_os_error', 0x4052cd)
        assert self.out_config.is_statically_linked('___doserrno', 0x4052f0)
        assert self.out_config.is_statically_linked('__errno', 0x405303)
        assert self.out_config.is_statically_linked('___acrt_uninitialize_winapi_thunks', 0x405809)
        assert self.out_config.is_statically_linked('__fcloseall', 0x40583f)
        assert self.out_config.is_statically_linked('__fflush_nolock', 0x405945)
        assert self.out_config.is_statically_linked('___acrt_stdio_free_buffer_nolock', 0x405a6d)
        assert self.out_config.is_statically_linked('___acrt_initialize_lowio', 0x405c17)
        assert self.out_config.is_statically_linked('___acrt_uninitialize_lowio', 0x405c6d)
        assert self.out_config.is_statically_linked('__isdigit_l', 0x405c99)
        assert self.out_config.is_statically_linked('__tolower_l', 0x405e65)
        assert self.out_config.is_statically_linked('__mbtowc_l', 0x405ef6)
        assert self.out_config.is_statically_linked('__wctomb_s_l', 0x40600a)
        assert self.out_config.is_statically_linked('_wctomb_s', 0x40612b)
        assert self.out_config.is_statically_linked('_strnlen', 0x406148)
        assert self.out_config.is_statically_linked('_wcsnlen', 0x40626f)
        assert self.out_config.is_statically_linked('___acrt_initialize_ptd', 0x4068a1)
        assert self.out_config.is_statically_linked('___acrt_uninitialize_ptd', 0x4068cd)
        assert self.out_config.is_statically_linked('___acrt_update_locale_info', 0x4068e7)
        assert self.out_config.is_statically_linked('___acrt_fp_format', 0x40720c)
        assert self.out_config.is_statically_linked('__fileno', 0x407356)
        assert self.out_config.is_statically_linked('__fputc_nolock', 0x40737c)
        assert self.out_config.is_statically_linked('__get_printf_count_output', 0x4073a5)
        assert self.out_config.is_statically_linked('___acrt_stdio_begin_temporary_buffering_nolock', 0x4073ba)
        assert self.out_config.is_statically_linked('___acrt_stdio_end_temporary_buffering_nolock', 0x40746f)
        assert self.out_config.is_statically_linked('__setmbcp_nolock', 0x407ef0)
        assert self.out_config.is_statically_linked('_memcpy_s', 0x4080e1)
        assert self.out_config.is_statically_linked('__ismbblead', 0x4081bb)
        assert self.out_config.is_statically_linked('___dcrt_get_narrow_environment_from_os', 0x40820a)
        assert self.out_config.is_statically_linked('___acrt_lock', 0x408619)
        assert self.out_config.is_statically_linked('___acrt_uninitialize_locks', 0x408630)
        assert self.out_config.is_statically_linked('___acrt_unlock', 0x408661)
        assert self.out_config.is_statically_linked('___acrt_lowio_create_handle_array', 0x408678)
        assert self.out_config.is_statically_linked('___acrt_lowio_destroy_handle_array', 0x4086f2)
        assert self.out_config.is_statically_linked('___acrt_lowio_ensure_fh_exists', 0x408727)
        assert self.out_config.is_statically_linked('___acrt_lowio_lock_fh', 0x4087bf)
        assert self.out_config.is_statically_linked('___acrt_lowio_unlock_fh', 0x4087e2)
        assert self.out_config.is_statically_linked('__free_osfhnd', 0x408805)
        assert self.out_config.is_statically_linked('__get_osfhandle', 0x408896)
        assert self.out_config.is_statically_linked('___pctype_func', 0x408900)
        assert self.out_config.is_statically_linked('___acrt_locale_free_monetary', 0x408926)
        assert self.out_config.is_statically_linked('___acrt_locale_free_numeric', 0x408a24)
        assert self.out_config.is_statically_linked('___acrt_locale_free_time', 0x408ac9)
        assert self.out_config.is_statically_linked('___acrt_GetStringTypeA', 0x408bad)
        assert self.out_config.is_statically_linked('__freea_crt', 0x408cca)
        assert self.out_config.is_statically_linked('___acrt_add_locale_ref', 0x408cea)
        assert self.out_config.is_statically_linked('___acrt_free_locale', 0x408d67)
        assert self.out_config.is_statically_linked('___acrt_locale_add_lc_time_reference', 0x408eb1)
        assert self.out_config.is_statically_linked('___acrt_locale_free_lc_time_if_unreferenced', 0x408eda)
        assert self.out_config.is_statically_linked('___acrt_locale_release_lc_time_reference', 0x408f0a)
        assert self.out_config.is_statically_linked('___acrt_release_locale_ref', 0x408f33)
        assert self.out_config.is_statically_linked('___acrt_update_thread_locale_data', 0x408fb4)
        assert self.out_config.is_statically_linked('__updatetlocinfoEx_nolock', 0x40902b)
        assert self.out_config.is_statically_linked('__recalloc_base', 0x409086)
        assert self.out_config.is_statically_linked('___acrt_initialize_heap', 0x4090f3)
        assert self.out_config.is_statically_linked('___acrt_execute_initializers', 0x40910e)
        assert self.out_config.is_statically_linked('___acrt_execute_uninitializers', 0x409191)
        assert self.out_config.is_statically_linked('__callnewh', 0x4091f2)
        assert self.out_config.is_statically_linked('__query_new_handler', 0x409236)
        assert self.out_config.is_statically_linked('___acrt_get_sigabrt_handler', 0x409374)
        assert self.out_config.is_statically_linked('___acrt_initialize_signal_handlers', 0x40938b)
        assert self.out_config.is_statically_linked('___hw_cw_sse2', 0x4095d7)
        assert self.out_config.is_statically_linked('__clearfp', 0x409682)
        assert self.out_config.is_statically_linked('__control87', 0x409760)
        assert self.out_config.is_statically_linked('__hw_cw', 0x409a62)
        assert self.out_config.is_statically_linked('__isctype_l', 0x409afb)
        assert self.out_config.is_statically_linked('___acrt_DownlevelLocaleNameToLCID', 0x409c89)
        assert self.out_config.is_statically_linked('__fclose_nolock', 0x409cb5)
        assert self.out_config.is_statically_linked('_fclose', 0x409d2b)
        assert self.out_config.is_statically_linked('__commit', 0x409e6b)
        assert self.out_config.is_statically_linked('__write', 0x40a46a)
        assert self.out_config.is_statically_linked('__isleadbyte_l', 0x40a761)
        assert self.out_config.is_statically_linked('___acrt_LCMapStringA', 0x40a9b7)
        assert self.out_config.is_statically_linked('___acrt_fp_strflt_to_string', 0x40aa02)
        assert self.out_config.is_statically_linked('__isatty', 0x40c522)
        assert self.out_config.is_statically_linked('_strpbrk', 0x40cac0)
        assert self.out_config.is_statically_linked('__mbsdec', 0x40cb00)
        assert self.out_config.is_statically_linked('__mbsdec_l', 0x40cb17)
        assert self.out_config.is_statically_linked('__strnicoll_l', 0x40cbdc)
        assert self.out_config.is_statically_linked('__realloc_base', 0x40ccd9)
        assert self.out_config.is_statically_linked('___set_fpsr_sse2', 0x40cd42)
        assert self.out_config.is_statically_linked('__clrfp', 0x40cdb8)
        assert self.out_config.is_statically_linked('__ctrlfp', 0x40cdcb)
        assert self.out_config.is_statically_linked('__set_statfp', 0x40cdf7)
        assert self.out_config.is_statically_linked('__statfp', 0x40ce52)
        assert self.out_config.is_statically_linked('__close', 0x40cf0e)
        assert self.out_config.is_statically_linked('__close_nolock', 0x40cf8d)
        assert self.out_config.is_statically_linked('__lseeki64', 0x40d1e7)
        assert self.out_config.is_statically_linked('__lseeki64_nolock', 0x40d202)
        assert self.out_config.is_statically_linked('__putwch_nolock', 0x40d21d)
        assert self.out_config.is_statically_linked('___strncnt', 0x40d262)
        assert self.out_config.is_statically_linked('_fegetenv', 0x40d27e)
        assert self.out_config.is_statically_linked('_fesetenv', 0x40d29b)
        assert self.out_config.is_statically_linked('_feholdexcept', 0x40d2e4)
        assert self.out_config.is_statically_linked('_acos', 0x40d340)
        assert self.out_config.is_statically_linked('__CIlog10_default', 0x40d3bb)
        assert self.out_config.is_statically_linked('__ceil_pentium4', 0x40d4d0)
        assert self.out_config.is_statically_linked('___acrt_stdio_allocate_buffer_nolock', 0x40d5ad)
        assert self.out_config.is_statically_linked('__strnicmp_l', 0x40d676)
        assert self.out_config.is_statically_linked('___acrt_CompareStringA', 0x40d9d5)
        assert self.out_config.is_statically_linked('___dcrt_lowio_initialize_console_output', 0x40da1d)
        assert self.out_config.is_statically_linked('___dcrt_terminate_console_input', 0x40da3c)
        assert self.out_config.is_statically_linked('___get_machine_status_sse2', 0x40dc34)
        assert self.out_config.is_statically_linked('___get_machine_status_x87', 0x40dc95)
        assert self.out_config.is_statically_linked('__getfpcontrolword', 0x40dcf6)
        assert self.out_config.is_statically_linked('__getfpstatusword', 0x40dd39)
        assert self.out_config.is_statically_linked('__setfpcontrolword', 0x40dde1)
        assert self.out_config.is_statically_linked('__setfpstatusword', 0x40de61)
        assert self.out_config.is_statically_linked('__CIlog10_pentium4', 0x40df00)
        assert self.out_config.is_statically_linked('__trandisp1', 0x40e390)
        assert self.out_config.is_statically_linked('__trandisp2', 0x40e3f7)
        assert self.out_config.is_statically_linked('__convertTOStoQNaN', 0x40e5bc)
        assert self.out_config.is_statically_linked('__fload_withFB', 0x40e5d5)
        assert self.out_config.is_statically_linked('__checkTOS_withFB', 0x40e618)
        assert self.out_config.is_statically_linked('__math_exit', 0x40e63b)
        assert self.out_config.is_statically_linked('__check_range_exit', 0x40e679)
        assert self.out_config.is_statically_linked('__startTwoArgErrorHandling', 0x40e720)
        assert self.out_config.is_statically_linked('__startOneArgErrorHandling', 0x40e737)
        assert self.out_config.is_statically_linked('___libm_error_support', 0x40e773)
        assert self.out_config.is_statically_linked('__ceil_default', 0x40e98b)
        assert self.out_config.is_statically_linked('___ascii_strnicmp', 0x40ea50)
        assert self.out_config.is_statically_linked('__d_inttype', 0x40eab1)
        assert self.out_config.is_statically_linked('__powhlp', 0x40eb1b)
        assert self.out_config.is_statically_linked('__87except', 0x40ec46)
        assert self.out_config.is_statically_linked('__frnd', 0x40ed51)
        assert self.out_config.is_statically_linked('__errcode', 0x40ed67)
        assert self.out_config.is_statically_linked('__except1', 0x40ed9b)
        assert self.out_config.is_statically_linked('__handle_exc', 0x40ee69)
        assert self.out_config.is_statically_linked('__raise_exc', 0x40f049)
        assert self.out_config.is_statically_linked('__raise_exc_ex', 0x40f06c)
        assert self.out_config.is_statically_linked('__set_errno_from_matherr', 0x40f35d)
        assert self.out_config.is_statically_linked('__umatherr', 0x40f38c)
        assert self.out_config.is_statically_linked('__decomp', 0x40f42e)
        assert self.out_config.is_statically_linked('__set_exp', 0x40f502)
        assert self.out_config.is_statically_linked('__sptype', 0x40f531)
        assert self.out_config.is_statically_linked('__fpclass', 0x40f58f)
        assert self.out_config.is_statically_linked('__FindPESection', 0x40f640)
        assert self.out_config.is_statically_linked('__IsNonwritableInCurrentImage', 0x40f690)
        assert self.out_config.is_statically_linked('__ValidateImageBase', 0x40f750)
        assert self.out_config.is_statically_linked('__aulldvrm', 0x40f790)
        assert self.out_config.is_statically_linked('__SEH_prolog4_GS', 0x40f830)
        assert self.out_config.is_statically_linked('__SEH_epilog4_GS', 0x40f879)
        assert self.out_config.is_statically_linked('__allmul', 0x40f890)
        assert self.out_config.is_statically_linked('__alldvrm', 0x40f8d0)
        assert self.out_config.is_statically_linked('__alloca_probe_16', 0x40f9d0)
        assert self.out_config.is_statically_linked('__chkstk', 0x40fa00)
        assert self.out_config.is_statically_linked('__ftol2_sse_excpt', 0x40fa6c)
        assert self.out_config.is_statically_linked('__ftol2', 0x40fa90)
        assert self.out_config.is_statically_linked('_strrchr', 0x410610)
        assert self.out_config.is_statically_linked('_strchr', 0x410750)
