/*
A KBase module: CompoundSetUtils
Contains tools for import & export of compound sets
*/

module CompoundSetUtils {
    typedef string obj_ref;

    typedef structure {
        string workspace_id;
        string staging_file_path;
        string compound_set_name;
        string mol2_staging_file_path;
    } compoundset_upload_params;

    typedef structure {
        string report_name;
        string report_ref;
        obj_ref compoundset_ref;
    } compoundset_upload_results;

    /*
        CompoundSetFromFile
        string staging_file_path
    */

    funcdef compound_set_from_file(compoundset_upload_params params)
        returns (compoundset_upload_results output) authentication required;

    typedef structure {
        string file_path;
        string packed_mol2_files_path;
        mapping<string, string> comp_id_mol2_file_name_map;
    } compoundset_download_results;

    typedef structure {
        string compound_set_ref;
        string output_format;
    } compoundset_download_params;

    /*
        CompoundSetToFile
        string compound_set_name
        string output_format
    */

    funcdef compound_set_to_file(compoundset_download_params params)
        returns (compoundset_download_results output) authentication required;

    typedef structure {
        string workspace_id;
        string model_ref;
        string compound_set_name;
    } compoundset_from_model_params;

    /*
        CompoundSetFromModel
        required:
        string workspace_id
        string model_ref
        string compound_set_name
    */

    funcdef compound_set_from_model(compoundset_from_model_params params)
        returns (compoundset_upload_results output) authentication required;

    /*  input and output structure functions for standard downloaders */
    typedef structure {
        string input_ref;
    } ExportParams;

    typedef structure {
        string shock_id;
    } ExportOutput;

    funcdef export_compoundset_as_tsv(ExportParams params)
        returns (ExportOutput output) authentication required;

    funcdef export_compoundset_as_sdf(ExportParams params)
        returns (ExportOutput output) authentication required;

    typedef structure {
        string packed_mol2_files_path;
        mapping<string, string> comp_id_mol2_file_name_map;
    } export_mol2_files_results;

    funcdef export_compoundset_mol2_files(ExportParams params)
        returns (export_mol2_files_results output) authentication required;

    typedef structure {
        string packed_pdbqt_files_path;
        mapping<string, string> comp_id_pdbqt_file_name_map;
    } convert_mol2_files_results;

    funcdef convert_compoundset_mol2_files_to_pdbqt(ExportParams params)
        returns (convert_mol2_files_results output) authentication required;

    typedef structure {
        string workspace_id;
        obj_ref compoundset_ref;
        int over_write;
    } FetchZINCMol2Params;

    /*
    mol2_files_dir: only contains mol2 files fetched from ZINC database.
    */
    typedef structure {
        string report_name;
        string report_ref;
        obj_ref compoundset_ref;
        string mol2_files_dir;
    } fetch_zinc_mol2_results;

    funcdef fetch_mol2_files_from_zinc(FetchZINCMol2Params params)
        returns (fetch_zinc_mol2_results output) authentication required;

};
