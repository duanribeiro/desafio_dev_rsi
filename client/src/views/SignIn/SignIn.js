import React, { useState, useEffect } from 'react';
import { Link as RouterLink, withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import validate from 'validate.js';
import { KeyboardDatePicker, MuiPickersUtilsProvider } from "material-ui-pickers";
import { makeStyles } from '@material-ui/styles';
import {
  Grid,
  Button,
  IconButton,
  TextField,
  Link,
  Typography
} from '@material-ui/core';

import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import axios from 'axios';
import DateFnsUtils from '@date-io/date-fns';


import { Facebook as FacebookIcon, Google as GoogleIcon } from 'icons';

const schema = {
  email: {
    presence: { allowEmpty: false, message: 'is required' },
    email: true,
    length: {
      maximum: 64
    }
  },
  password: {
    presence: { allowEmpty: false, message: 'is required' },
    length: {
      maximum: 128
    }
  }
};

const useStyles = makeStyles(theme => ({
  root: {
    backgroundColor: theme.palette.background.default,
    height: '100%'
  },
  grid: {
    height: '100%'
  },
  quoteContainer: {
    [theme.breakpoints.down('md')]: {
      display: 'none'
    }
  },
  quote: {
    backgroundColor: theme.palette.neutral,
    height: '100%',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundImage: 'url(/images/auth.jpg)',
    backgroundSize: 'cover',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center'
  },
  quoteInner: {
    textAlign: 'center',
    flexBasis: '600px'
  },
  quoteText: {
    color: theme.palette.white,
    fontWeight: 300
  },
  name: {
    marginTop: theme.spacing(3),
    color: theme.palette.white
  },
  bio: {
    color: theme.palette.white
  },
  contentContainer: {},
  content: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column'
  },
  contentHeader: {
    display: 'flex',
    alignItems: 'center',
    paddingTop: theme.spacing(5),
    paddingBototm: theme.spacing(2),
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2)
  },
  logoImage: {
    marginLeft: theme.spacing(4)
  },
  contentBody: {
    flexGrow: 1,
    display: 'flex',
    alignItems: 'center',
    [theme.breakpoints.down('md')]: {
      justifyContent: 'center'
    }
  },
  form: {
    paddingLeft: 100,
    paddingRight: 100,
    paddingBottom: 125,
    flexBasis: 700,
    [theme.breakpoints.down('sm')]: {
      paddingLeft: theme.spacing(2),
      paddingRight: theme.spacing(2)
    }
  },
  title: {
    marginTop: theme.spacing(3)
  },
  socialButtons: {
    marginTop: theme.spacing(3)
  },
  socialIcon: {
    marginRight: theme.spacing(1)
  },
  sugestion: {
    marginTop: theme.spacing(2)
  },
  textField: {
    marginTop: theme.spacing(2)
  },
  signInButton: {
    margin: theme.spacing(2, 0)
  }
}));

const SignIn = props => {
  const { history } = props;

  const classes = useStyles();

  const [formState, setFormState] = useState({
    isValid: false,
    values: {},
    touched: {},
    errors: {}
  });

  useEffect(() => {
    const errors = formState.cpf ? false : true

    setFormState(formState => ({
      ...formState,
      errors: errors || {}
    }));
  }, [formState.values]);

  const handleBack = () => {
    history.goBack();
  };

  const handleChange = event => {
    event.persist();

    setFormState(formState => ({
      ...formState,
      values: {
        ...formState.values,
        [event.target.name]:
          event.target.type === 'checkbox'
            ? event.target.checked
            : event.target.value
      },
      touched: {
        ...formState.touched,
        [event.target.name]: true
      }
    }));
  };

  const handleSignIn = event => {
    event.preventDefault();
    history.push('/dashboard');
  };


  const hasError = field =>
    formState.touched[field] && formState.errors[field] ? true : false;
    
 const [open, setOpen] = React.useState(false);

  function handleClickOpen() {
    setOpen(true);
  }

  function handleClose() {
    setOpen(false);
  }
  const [inputs, setInputs] = React.useState({ })
  const handleDateChange = date => {
    formState.values.dataNascimento = date.toString()
  }

  const checkForm1 = () => formState.values.cpf && formState.values.password ? false : true


  // Aqui temos o envio de informações do formulário para o backend
  const handleSubmit = event => {
      event.preventDefault()
      axios.post(`${process.env.REACT_APP_ATLAS_API}/usuario`, formState.values, {
        "headers": {
          "Authorization": ''
        }
      })
        .then(response => {
          window.alert("Usuário criado com sucesso!")
          window.location.reload()
        })
        .catch(error => {
          console.error(error.message)
      })
    }

      // Aqui temos o envio de informações do formulário para o backend
  const handleLogin = event => {
    event.preventDefault()
    axios.post(`${process.env.REACT_APP_ATLAS_API}/usuario/login`, formState.values, {
      "headers": {
        "Authorization": ''
      }
    })
      .then(response => {
        window.location.href= '/dashboard'
      })
      .catch(error => {
        window.alert("Usuário ou senha incorreta!")
    })
  }
    

  return (

    <div className={classes.root}>
     
      <Grid
        className={classes.grid}
        container
      >
        <Grid
          className={classes.quoteContainer}
          item
          lg={5}
        >
          <div className={classes.quote}>
            <div className={classes.quoteInner}>
              <Typography
                className={classes.quoteText}
                variant="h1"
              >
              </Typography>

            </div>
          </div>
        </Grid>
        <Grid
          className={classes.content}
          item
          lg={7}
          xs={12}
        >
          <div className={classes.content}>
            <div className={classes.contentBody} >
              <form
                className={classes.form}
                onSubmit={handleLogin}
              >
                <Typography
                  align="center"
                  className={classes.title}
                  variant="h2"
                >
                  ATLAS
                </Typography>

                <Typography
                  align="center"
                  className={classes.sugestion}
                  color="textSecondary"
                  variant="body1"
                >
                  Autentique-se para ter acesso.
                </Typography>
                <TextField
                  className={classes.textField}
                  error={hasError('cpf')}
                  fullWidth
                  helperText={
                    hasError('cpf') ? formState.errors.cpf[0] : null
                  }
                  label="CPF"
                  name="cpf"
                  onChange={handleChange}
                  type="text"
                  value={formState.values.cpf}
                  variant="outlined"
                />
                <TextField
                  className={classes.textField}
                  error={hasError('password')}
                  fullWidth
                  helperText={
                    hasError('password') ? formState.errors.password[0] : null
                  }
                  label="Senha"
                  name="password"
                  onChange={handleChange}
                  type="password"
                  value={formState.values.password}
                  variant="outlined"
                />
                <Button
                  className={classes.signInButton}
                  color="primary"
                  
                  fullWidth
                  size="large"
                  type="submit"
                  variant="contained"
                >
                  AUTENTICAR
                </Button>

                <Typography
                  color="textSecondary"
                  variant="body1"
                >
                  Não tem conta?
                  </Typography>

                  <Link to="">
                    <Typography
                      variant="h6"
                      onClick={handleClickOpen}
                      style={{"color": "blue"}}
                    >
                      CRIE UMA JÁ!
                    </Typography>
                  </Link>
        
              </form>
            </div>
          </div>
          <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
        <DialogTitle style={{"width":"900px"}} id="form-dialog-title">Cadastrar novo usuário</DialogTitle>
        <DialogContent>
          <TextField
            required
            className={classes.textField}
            error={hasError('nome')}
            fullWidth
            helperText={
              hasError('nome') ? formState.errors.nome[0] : null
            }
            label="Nome"
            name="nome"
            onChange={handleChange}
            type="text"
            value={formState.values.nome || ''}
          />
          <TextField
            required
            className={classes.textField}
            error={hasError('cpf')}
            fullWidth
            helperText={
              hasError('cpf') ? formState.errors.bairro[0] : null
            }
            label="CPF"
            name="cpf"
            onChange={handleChange}
            type="text"
            value={formState.values.cpf || ''}
          />
          <TextField
            required
            className={classes.textField}
            error={hasError('password')}
            fullWidth
            helperText={
              hasError('password') ? formState.errors.password[0] : null
            }
            label="Password"
            name="password"
            onChange={handleChange}
            type="password"
            value={formState.values.password || ''}
          />
           <TextField
            required
            className={classes.textField}
            error={hasError('email')}
            fullWidth
            helperText={
              hasError('email') ? formState.errors.email[0] : null
            }
            label="Email address"
            name="email"
            onChange={handleChange}
            type="text"
            value={formState.values.email || ''}
          />
          <TextField
            required
            className={classes.textField}
            error={hasError('bairro')}
            fullWidth
            helperText={
              hasError('bairro') ? formState.errors.bairro[0] : null
            }
            label="Bairro"
            name="bairro"
            onChange={handleChange}
            type="text"
            value={formState.values.bairro || ''}
          />
          <TextField
            required
            className={classes.textField}
            error={hasError('cidade')}
            fullWidth
            helperText={
              hasError('cidade') ? formState.errors.bairro[0] : null
            }
            label="Cidade"
            name="cidade"
            onChange={handleChange}
            type="text"
            value={formState.values.cidade || ''}
          />
          <TextField
          required
            className={classes.textField}
            error={hasError('complemento')}
            fullWidth
            helperText={
              hasError('complemento') ? formState.errors.bairro[0] : null
            }
            label="Complemento"
            name="complemento"
            onChange={handleChange}
            type="text"
            value={formState.values.complemento || ''}
          />

          <TextField
          required
            className={classes.textField}
            error={hasError('dataNascimento')}
            fullWidth
            helperText={
              hasError('dataNascimento') ? formState.errors.bairro[0] : null
            }
            label="Data de Nascimento"
            name="dataNascimento"
            onChange={handleChange}
            type="text"
            value={formState.values.dataNascimento || ''}
          />
          <TextField
          required
            className={classes.textField}
            error={hasError('pais')}
            fullWidth
            helperText={
              hasError('pais') ? formState.errors.bairro[0] : null
            }
            label="País"
            name="pais"
            onChange={handleChange}
            type="text"
            value={formState.values.pais || ''}
          />
          
          <TextField
          required
            className={classes.textField}
            error={hasError('rua')}
            fullWidth
            helperText={
              hasError('rua') ? formState.errors.bairro[0] : null
            }
            label="Rua"
            name="rua"
            onChange={handleChange}
            type="text"
            value={formState.values.rua || ''}
          />
          <TextField
          required
            className={classes.textField}
            error={hasError('sobrenome')}
            fullWidth
            helperText={
              hasError('sobrenome') ? formState.errors.sobrenome[0] : null
            }
            label="Sobrenome"
            name="sobrenome"
            onChange={handleChange}
            type="text"
            value={formState.values.sobrenome || ''}
          />
         
          <TextField
          required
            className={classes.textField}
            error={hasError('estado')}
            fullWidth
            helperText={
              hasError('estado') ? formState.errors.estado[0] : null
            }
            label="Estado"
            name="estado"
            onChange={handleChange}
            type="text"
            value={formState.values.estado || ''}
          />
          <TextField
          required
            className={classes.textField}
            error={hasError('numero')}
            fullWidth
            helperText={
              hasError('numero') ? formState.errors.numero[0] : null
            }
            label="Número"
            name="numero"
            onChange={handleChange}
            type="text"
            value={formState.values.numero || ''}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="secondary">
            Cancelar
          </Button>
          <Button onClick={handleSubmit}  color="secondary">
            Cadastrar
          </Button>
        </DialogActions>
      </Dialog>


      
        </Grid>
      </Grid>
    </div>
  );
};

SignIn.propTypes = {
  history: PropTypes.object
};

export default withRouter(SignIn);
