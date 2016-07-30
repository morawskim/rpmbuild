# Modified version of what `composer _completion -g -p composer` generates
# Composer will only load plugins when a valid composer.json is in its working directory,
# so  for this hack to work, we are always running the completion command in ~/.composer
function _composercomplete {
    export COMP_LINE COMP_POINT COMP_WORDBREAKS;
    local -x COMPOSER_CWD=`pwd`
    local RESULT STATUS

    # Honour the COMPOSER_HOME variable if set
    local composer_dir=$COMPOSER_HOME
    if [ -z "$composer_dir" ]; then
        composer_dir=$HOME/.composer
    fi

    RESULT=`cd $composer_dir && composer depends _completion`;
    STATUS=$?;

    if [ $STATUS -ne 0 ]; then
        echo $RESULT;
        return $?;
    fi;

    local cur;
    _get_comp_words_by_ref -n : cur;

    COMPREPLY=(`compgen -W "$RESULT" -- $cur`);

    __ltrim_colon_completions "$cur";
};
complete -F _composercomplete composer;